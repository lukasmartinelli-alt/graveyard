package org.syncany.plugins.googledrive;

import com.google.api.services.drive.model.File;
import com.google.api.services.drive.model.ParentReference;

import java.io.IOException;
import java.util.*;

public class GoogleDrivePathMap extends HashMap<String, String> {
    private final static String ROOT_ID = "root";
    private List<File> files = new ArrayList<>();

    public GoogleDrivePathMap build(List<File> files) throws IOException {
        this.files = files;
        populateRecursive("/", ROOT_ID);
        return this;
    }

    private List<File> getChildren(String parentId) {
        List<File> children = new ArrayList<>();
        for(File entry : files) {
            for(ParentReference parent : entry.getParents()) {
                if(parent.getId().equals(parentId) || parent.getIsRoot() && parentId.equals(ROOT_ID)) {
                    children.add(entry);
                }
            }
        }
        return children;
    }

    private void populateRecursive(String path, String parentId) {
        for(File child : getChildren(parentId)) {
            if(!child.getTitle().isEmpty()) {
                String childPath = new java.io.File(path, child.getTitle()).getPath();

                put(childPath, child.getId());
                populateRecursive(childPath, child.getId());
            }
        }
    }
}
