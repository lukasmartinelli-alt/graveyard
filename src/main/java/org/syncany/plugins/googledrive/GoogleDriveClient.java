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

}


