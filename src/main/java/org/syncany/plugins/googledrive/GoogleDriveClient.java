package org.syncany.plugins.googledrive;

import com.google.api.client.http.FileContent;
import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.*;
import com.google.api.services.drive.model.File;
import org.syncany.plugins.transfer.StorageException;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class GoogleDriveClient {
    private static final String FOLDER_MIMETYPE = "application/vnd.google-apps.folder";
    private final Drive client;

    public GoogleDriveClient(Drive client) {
        this.client = client;
    }

    public About about() throws IOException {
        return client.about().get().execute();
    }

    public List<File> allFiles() throws IOException {
        List<File> results = new ArrayList<>();
        Drive.Files.List request = this.client.files().list().setQ("'appfolder' in parents");

        do {
            FileList files = request.execute();
            results.addAll(files.getItems());
            request.setPageToken(files.getNextPageToken());
        } while (request.getPageToken() != null &&
                !request.getPageToken().isEmpty());

        return results;
    }

    public boolean folderExists(Path path) throws IOException {
        PathMap paths = new PathMap().build(allFiles());

        if(paths.containsKey(path)) {
            String fileId = paths.get(path);
            File folder = this.client.files().get(fileId).execute();
            return folder.getMimeType().equals(FOLDER_MIMETYPE);
        }

        return false;
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
        PathMap paths = new PathMap().build(allFiles());

        String parentPath = Paths.get(path).getParent().toString();
        String parentId = paths.get(parentPath);
        List<ParentReference> parents = new ArrayList<>();
        parents.add(new ParentReference().setId(parentId));

        return parents;
    }

    private String find(Path remotePath) throws IOException {
        PathMap paths = new PathMap().build(allFiles());

        if(paths.containsKey(remotePath)) {
            return paths.get(remotePath);
        }
        throw new FileNotFoundException(remotePath + " does not exist.");
    }

    public File uploadFile(Path remoteFilePath, java.io.File localFile) throws IOException {
        String mimeType = "foo";
        File remoteMetadata = new File()
                .setTitle(remoteFilePath.getFileName().toString())
                .setParents(createParents(remoteFilePath.toString()));
        FileContent remoteMedia = new FileContent(mimeType, localFile);

        return client.files().insert(remoteMetadata, remoteMedia).execute();
    }

    public void downloadFile(Path remoteFilePath, OutputStream localStream) throws IOException {
        String remoteId = find(remoteFilePath);
        client.files().get(remoteId).executeMediaAndDownloadTo(localStream);
    }

    public void delete(Path remotePath) throws IOException {
        String remoteId = find(remotePath);
        client.files().delete(remoteId);
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

    public void move(Path sourceRemotePath, Path targetRemotePath) throws IOException {
        String sourceRemoteId = find(sourceRemotePath);
        String targetRemoteId = find(targetRemotePath);

        ParentList targetParents = client.parents().list(targetRemoteId).execute();
        ParentList sourceParents = client.parents().list(sourceRemoteId).execute();

        if(targetParents.getItems().size() == 0) {
            throw new IOException("Target has no parents");
        }

        for(ParentReference parent : sourceParents.getItems()) {
            client.parents().delete(parent.getId(), sourceRemoteId);
        }

        ParentReference parent = targetParents.getItems().get(0);
        client.parents().insert(parent.getId(), parent);
    }
}


