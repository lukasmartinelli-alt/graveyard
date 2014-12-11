package org.syncany.plugins.googledrive;

import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.File;
import junit.framework.Assert;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.UUID;

public class GoogledriveClientTest {
    private static final HttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    private static final JsonFactory JSON_FACTORY = new JacksonFactory();
    private static final String ACCESS_TOKEN = "ya29.2QBPOL_FWfr0F1tC9N6RxBS9i3rmyiVJrziImwmh-zn4Mk16aBks90lK5aqifwNQWzqmUM5pgqY9GA";

    private GoogledriveClient client;
    private Path rootPath;

    /*
    private void printAccessToken() throws IOException {
        String authorizeUrl = GoogledriveTransferPlugin.getAuthorizationUrl();
        String authorizationToken = "";
        GoogleTokenResponse response = GoogledriveTransferPlugin.FLOW
                .newTokenRequest(authorizationToken)
                .setRedirectUri(GoogledriveTransferPlugin.REDIRECT_URI)
                .execute();
        System.out.println(response.getAccessToken());
    }*/

    @Before
    public void setUp() throws IOException {
        GoogleCredential credential = new GoogleCredential().setAccessToken(ACCESS_TOKEN);
        Drive wrappedClient = new Drive.Builder(HTTP_TRANSPORT, JSON_FACTORY, credential)
                .setApplicationName("Syncany Test Suite")
                .build();

        client = new GoogledriveClient(wrappedClient);
        rootPath = Paths.get("/test" + UUID.randomUUID());
        client.createFolder(rootPath);
    }

    @After
    public void tearDown() throws IOException {
        if(client.folderExists(rootPath)) {
            client.delete(rootPath);
        }
    }

    @Test
    public void testAbout() throws IOException {
        String name = client.about().getName();
        Assert.assertEquals("Testing Cuckoo Drive", name);
    }

    @Test
    public void testCreateFolder() throws IOException {
        client.createFolder(rootPath.resolve("folder"));
        Assert.assertTrue(client.folderExists(rootPath.resolve("folder")));
    }

    @Test
    public void testDeleteFolder() throws IOException {
        client.createFolder(rootPath.resolve("folder"));
        client.delete(rootPath.resolve("folder"));
        Assert.assertFalse(client.folderExists(rootPath.resolve("folder")));
    }

    @Test
    public void testList() throws IOException {
        client.createFolder(rootPath.resolve("folder"));
        client.createFolder(rootPath.resolve("folder/subfolder1"));
        client.createFolder(rootPath.resolve("folder/subfolder2"));

        List<File> listing = client.list(rootPath.resolve("folder"));
        Assert.assertEquals("subfolder2", listing.get(0).getTitle());
        Assert.assertEquals("subfolder1", listing.get(1).getTitle());
    }

    @Test
    public void testUpload() throws IOException {
        java.io.File tempLocalFile = java.io.File.createTempFile("file", ".bin");
        try(FileOutputStream outputStream = new FileOutputStream(tempLocalFile)) {
            outputStream.write(new byte[100]);
        }

        client.uploadFile(rootPath.resolve("file.bin"), tempLocalFile);

        Assert.assertTrue(client.fileExists(rootPath.resolve("file.bin")));
    }
}
