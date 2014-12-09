package org.syncany.plugins.googledrive;

import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.File;
import com.google.api.services.drive.model.ParentReference;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class GoogleDrivePathMap {
    private final Drive client;
    private List<File> files = new ArrayList<File>();
    private Map<String, String> pathMap = new TreeMap<>();

    public GoogleDrivePathMap(Drive client) {
        this.client = client;
    }

    public Map<String, String> build() {
        try {
            files = this.client.files().list().execute().getItems();
        } catch (IOException e) {
            e.printStackTrace();
        }
        populateMapRecursive("/");
        return pathMap;
    }

    private List<File> getChildren() {
        List<File> children = new ArrayList<>();
        for(File entry : files) {
            for(ParentReference parent : entry.getParents()) {
                if(parent.getIsRoot()) {
                    children.add(entry);
                }
            }
        }
        return children;
    }

    private List<File> getChildren(String parentId) {
        List<File> children = new ArrayList<>();
        for(File entry : files) {
            for(ParentReference parent : entry.getParents()) {
                if(parent.getId().equals(parentId)) {
                    children.add(entry);
                }
            }
        }
        return children;
    }

    private void populateMapRecursive(String path) {
        for(File child : getChildren()) {
            if(!child.getTitle().isEmpty()) {
                String childPath = path + child.getTitle();
                pathMap.put(childPath, child.getId());
                populateMapRecursive(childPath, child.getId());
            }
        }
    }

    private void populateMapRecursive(String path, String parentId) {
        for(File child : getChildren(parentId)) {
            if(!child.getTitle().isEmpty()) {
                String childPath = path + child.getTitle();
                pathMap.put(childPath, child.getId());
                populateMapRecursive(childPath, child.getId());
            }
        }
    }
}
