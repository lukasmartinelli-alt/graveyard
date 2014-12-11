package org.syncany.plugins.googledrive;

import com.google.api.client.http.FileContent;
import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.*;
import com.google.api.services.drive.model.File;

import javax.naming.OperationNotSupportedException;
import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class GoogledriveClient {
    private static final String FOLDER_MIMETYPE = "application/vnd.google-apps.folder";
    private static final String FILE_MIMETYPE = "application/x-syncany";
    private final Drive client;
    private final String rootId;

    public GoogledriveClient(Drive client) throws IOException {
        this.client = client;
        this.rootId = client.files().get("appfolder").execute().getId();
    }

    public About about() throws IOException {
        return client.about().get().execute();
    }

    public List<File> allFiles() throws IOException {
        List<File> results = new ArrayList<>();
        Drive.Files.List request = this.client.files().list();

        do {
            FileList files = request.execute();
            results.addAll(files.getItems());
            request.setPageToken(files.getNextPageToken());
        } while (request.getPageToken() != null &&
                !request.getPageToken().isEmpty());

        return results;
    }

    public boolean folderExists(Path remotePath) {
        try {
            String remoteId = find(remotePath);
            File folder = this.client.files().get(remoteId).execute();
            return folder.getMimeType().equals(FOLDER_MIMETYPE);
        } catch(IOException e) {
            return false;
        }
    }

    public boolean fileExists(Path remotePath) {
        try {
            String remoteId = find(remotePath);
            File file = this.client.files().get(remoteId).execute();
            return !file.getMimeType().equals(FOLDER_MIMETYPE);
        } catch (IOException e) {
            return false;
        }
    }

    public void createFolder(Path path) throws IOException {
        File folder = new File()
                .setTitle(path.getFileName().toString())
                .setParents(createParents(path.toString()))
                .setMimeType(FOLDER_MIMETYPE);

        client.files().insert(folder).execute();
    }

    private List<ParentReference> createParents(String path) throws IOException {
        PathMap paths = new PathMap(rootId).build(allFiles());

        String parentPath = Paths.get(path).getParent().toString();
        if(paths.containsKey(parentPath)) {
            String parentId = paths.get(parentPath);
            List<ParentReference> parents = new ArrayList<>();
            parents.add(new ParentReference().setId(parentId));

            return parents;
        } else {
            throw new IndexOutOfBoundsException(path + " is not found in path map");
        }
    }

    private String find(Path remotePath) throws IOException {
        PathMap paths = new PathMap(rootId).build(allFiles());

        if(paths.containsKey(remotePath.toString())) {
            return paths.get(remotePath.toString());
        }
        throw new FileNotFoundException(remotePath + " does not exist.");
    }

    public File uploadFile(Path remoteFilePath, java.io.File localFile) throws IOException {
        File remoteMetadata = new File()
                .setTitle(remoteFilePath.getFileName().toString())
                .setParents(createParents(remoteFilePath.toString()));
        FileContent remoteMedia = new FileContent(FILE_MIMETYPE, localFile);

        return client.files().insert(remoteMetadata, remoteMedia).execute();
    }

    public void downloadFile(Path remoteFilePath, OutputStream localStream) throws IOException {
        String remoteId = find(remoteFilePath);
        client.files().get(remoteId).executeMediaAndDownloadTo(localStream);
    }

    public void delete(Path remotePath) throws IOException {
        String remoteId = find(remotePath);
        deleteRecursive(remoteId);
    }

    private void deleteRecursive(String remoteId) throws IOException {
        for(ChildReference child : client.children().list(remoteId).execute().getItems()) {
            deleteRecursive(child.getId());
        }
        client.files().delete(remoteId).execute();
    }

    public List<File> list(Path remotePath) throws IOException {
        String remoteId = find(remotePath);
        ChildList children = client.children().list(remoteId).execute();
        List<File> results = new ArrayList<>();

        for (ChildReference child : children.getItems()) {
            results.add(client.files().get(child.getId()).execute());
        }

        return results;
    }

    public void move(Path sourceRemotePath, Path targetRemotePath) throws IOException, OperationNotSupportedException {
        String sourceRemoteId = find(sourceRemotePath);
        String targetRemoteParentId = find(targetRemotePath.getParent());

        File copy = client.files().get(sourceRemoteId).execute();
        if(copy.getMimeType().equals(FOLDER_MIMETYPE)) {
            throw new OperationNotSupportedException("Cannot move a folder by copying it.");
        }
        copy.setTitle(targetRemotePath.getFileName().toString());
        copy.setParents(Arrays.asList(new ParentReference().setId(targetRemoteParentId)));

        client.files().copy(sourceRemoteId, copy).execute();
        client.files().delete(sourceRemoteId).execute();
    }
}


