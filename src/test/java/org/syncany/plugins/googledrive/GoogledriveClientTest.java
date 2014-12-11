package org.syncany.plugins.googledrive;

import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.drive.Drive;
import com.google.api.services.drive.model.File;
import junit.framework.Assert;
import org.apache.commons.io.IOUtils;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import javax.naming.OperationNotSupportedException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.UUID;

public class GoogledriveClientTest {
    private static final HttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    private static final JsonFactory JSON_FACTORY = new JacksonFactory();
    private static final String ACCESS_TOKEN = "ya29.2QB5qRZX2N2Dh_AJn0CdXOSPHk6TYnqY5se3kOQzAqq5jy5C3PRhpdV51-dCZkjdrxJ786R5wVkN3w";
    private static final String REFRESH_TOKEN = "1/jH00Opu4gvpVWT9hVpKTL45oDcv352YhYHWifY-1RLcMEudVrK5jSpoR30zcRFq6";

    private GoogledriveClient client;
    private Path rootPath;

    private void clearAppfolder() throws IOException {
        for(File child : client.list(Paths.get("/"))) {
            client.delete(Paths.get("/", child.getTitle()));
        }
    }

    /*private void printAccessToken() throws IOException {
        String authorizeUrl = GoogledriveTransferPlugin.getAuthorizationUrl();
        String authorizationToken = "";
        com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse response = GoogledriveTransferPlugin.FLOW
                .newTokenRequest(authorizationToken)
                .setRedirectUri(GoogledriveTransferPlugin.REDIRECT_URI)
                .execute();
        System.out.println(response.getAccessToken());
    }*/

    @Before
    public void setUp() throws IOException {
        GoogleCredential credential = new GoogleCredential.Builder()
                .setClientSecrets(GoogledriveTransferPlugin.CLIENT_ID, GoogledriveTransferPlugin.CLIENT_SECRET)
                .setJsonFactory(GoogledriveTransferPlugin.FLOW.getJsonFactory())
                .setTransport(GoogledriveTransferPlugin.FLOW.getTransport()).build()
                .setAccessToken(ACCESS_TOKEN).setRefreshToken(REFRESH_TOKEN);
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

    @Test
    public void testDownload() throws IOException {
        java.io.File tempUploadFile = java.io.File.createTempFile("upload", ".bin");
        try(FileOutputStream outputStream = new FileOutputStream(tempUploadFile)) {
            outputStream.write(new byte[100]);
        }
        client.uploadFile(rootPath.resolve("upload.bin"), tempUploadFile);

        java.io.File tempDownloadFile = java.io.File.createTempFile("download", ".bin");
        try(FileOutputStream outputStream = new FileOutputStream(tempDownloadFile)) {
            client.downloadFile(rootPath.resolve("upload.bin"), outputStream);
        }

        try(FileInputStream inputStream = new FileInputStream(tempDownloadFile)) {
            byte[] bytes = IOUtils.toByteArray(inputStream);
            Assert.assertEquals(100, bytes.length);
        }
    }

    @Test
    public void testMoveFile() throws IOException, OperationNotSupportedException {
        java.io.File tempUploadFile = java.io.File.createTempFile("file", ".bin");
        try(FileOutputStream outputStream = new FileOutputStream(tempUploadFile)) {
            outputStream.write(new byte[100]);
        }
        client.uploadFile(rootPath.resolve("file.bin"), tempUploadFile);
        client.move(rootPath.resolve("file.bin"), rootPath.resolve("renamed.bin"));
        Assert.assertTrue(client.fileExists(rootPath.resolve("renamed.bin")));
        Assert.assertFalse(client.fileExists(rootPath.resolve("file.bin")));
    }

    @Test(expected=OperationNotSupportedException.class)
    public void testMoveDirectory() throws IOException, OperationNotSupportedException {
        client.createFolder(rootPath.resolve("folder"));
        client.move(rootPath.resolve("folder"), rootPath.resolve("renamed"));
    }
}
