package org.syncany.plugins.googledrive;

import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.About;
import com.google.api.services.drive.model.File;
import com.google.api.services.drive.model.FileList;
import com.google.api.services.drive.model.ParentReference;

import java.io.IOException;
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

    public void createFolder(String path) throws IOException {
        File folder = new File()
                .setTitle(new java.io.File(path).getName())
                .setParents(createParents(path))
                .setMimeType(FOLDER_MIMETYPE);

        client.files().insert(folder).execute();
    }

    private List<ParentReference> createParents(String path) throws IOException {
        PathMap paths = new PathMap().build(allFiles());

        String parentPath = new java.io.File(path).getParentFile().getPath();
        String parentId = paths.get(parentPath);
        List<ParentReference> parents = new ArrayList<>();
        parents.add(new ParentReference().setId(parentId));

        return parents;
    }
}


