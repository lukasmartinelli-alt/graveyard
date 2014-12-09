package org.syncany.plugins.googledrive;

import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.File;
import com.google.api.services.drive.model.FileList;
import com.google.api.services.drive.model.ParentReference;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class GoogleDriveClient {
    private static final String ROOT_FOLDER = "syncany-connector";
    private static final String FOLDER_MIMETYPE = "application/vnd.google-apps.folder";
    private final Drive client;

    public GoogleDriveClient(Drive client) {
        this.client = client;
    }


    private void ensureStructure() {
        Map<String, String> pathMap = new GoogleDrivePathMap(client).build();

        String rootId = pathMap.get("/");



    }
    private void createFolder(File parent) {
        File folder = new File().setMimeType(FOLDER_MIMETYPE);
        folder.setParents()
        this.client.files().insert(folder);
    }
}


