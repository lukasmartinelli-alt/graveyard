package org.syncany.plugins.googledrive;

import com.google.api.services.drive.model.File;
import com.google.api.services.drive.model.ParentReference;

import java.io.IOException;
import java.net.URI;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class PathMap extends HashMap<String, String> {
    private final static String ROOT_ID = "root";
    private List<File> files = new ArrayList<>();

    public PathMap build(List<File> files) throws IOException {
        this.files = files;
        populateRecursive("/", ROOT_ID);
        return this;
    }

    @Override
    public String get(Object o) {
        Path path = Paths.get((String) o);
        return super.get(path.normalize().toString());
    }

    @Override
    public String put(String key, String value) {
        return super.put(Paths.get(key).normalize().toString(), value);
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
                String childPath = Paths.get(path, child.getTitle()).toString();
                put(childPath, child.getId());
                populateRecursive(childPath, child.getId());
            }
        }
    }
}
