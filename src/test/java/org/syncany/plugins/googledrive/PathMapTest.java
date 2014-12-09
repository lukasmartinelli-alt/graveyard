package org.syncany.plugins.googledrive;

import com.google.api.services.drive.model.File;
import com.google.api.services.drive.model.ParentReference;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class PathMapTest {

    @Test
    public void testRecursiveLookup() throws IOException {
        List<File> files = new ArrayList<>();

        List<ParentReference> fooParents = new ArrayList<>();
        fooParents.add(new ParentReference().setId("root").setIsRoot(true));
        File foo= new File().setId("foo").setTitle("foolo").setParents(fooParents);
        files.add(foo);

        List<ParentReference> barParents = new ArrayList<>();
        barParents.add(new ParentReference().setId("foo").setIsRoot(false));
        File bar = new File().setId("bar").setTitle("bar.txt").setParents(barParents);
        files.add(bar);

        Map<String, String> pathMap = new PathMap().build(files);


        String[] paths = { "/foolo/bar.txt", "/foolo" };
        Assert.assertArrayEquals(paths, pathMap.keySet().toArray());
        Assert.assertEquals("foo", pathMap.get("/foolo"));
        Assert.assertEquals("bar", pathMap.get("/foolo/bar.txt"));
    }
}