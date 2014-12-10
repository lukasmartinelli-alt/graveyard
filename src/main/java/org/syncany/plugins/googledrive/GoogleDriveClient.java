package org.syncany.plugins.googledrive;

import com.google.api.client.http.FileContent;
import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.About;
import com.google.api.services.drive.model.File;
import com.google.api.services.drive.model.FileList;
import com.google.api.services.drive.model.ParentReference;

import java.io.ByteArrayInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
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

    public boolean folderExists(String path) throws IOException {
        PathMap paths = new PathMap().build(allFiles());

        if(paths.containsKey(path)) {
            String fileId = paths.get(path);
            File folder = this.client.files().get(fileId).execute();
            return folder.getMimeType().equals(FOLDER_MIMETYPE);
        }

        return false;
    }

    public boolean fileExists(String remotePath) {
        try {
            String remoteId = find(remotePath);
            File file = this.client.files().get(remoteId).execute();
            return !file.getMimeType().equals(FOLDER_MIMETYPE);
        } catch (IOException e) {
            return false;
        }
    }

    public void createFolder(String path) throws IOException {
        File folder = new File()
                .setTitle(new java.io.File(path).getName())
                .setParents(createParents(path))
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

    private String find(String remotePath) throws IOException {
        PathMap paths = new PathMap().build(allFiles());

        if(paths.containsKey(remotePath)) {
            return paths.get(remotePath);
        }
        throw new FileNotFoundException(remotePath + " does not exist.");
    }

    public File uploadFile(String remoteFilePath, java.io.File localFile) throws IOException {
        String mimeType = "foo";
        File remoteMetadata = new File()
                .setTitle(Paths.get(remoteFilePath).toString())
                .setParents(createParents(remoteFilePath));
        FileContent remoteMedia = new FileContent(mimeType, localFile);

        return client.files().insert(remoteMetadata, remoteMedia).execute();
    }

    public void delete(String remotePath) throws IOException {
        String remoteId = find(remotePath);
        client.files().delete(remoteId);
    }
}


