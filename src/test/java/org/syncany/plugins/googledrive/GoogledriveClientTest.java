package org.syncany.plugins.googledrive;

import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.drive.Drive;
import junit.framework.Assert;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class GoogledriveClientTest {
    private static final HttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    private static final JsonFactory JSON_FACTORY = new JacksonFactory();
    private static final String ACCESS_TOKEN = "ya29.2AAYUsf_PcIGLPzNHw2ST78g5BeKquoD4xCqXT4yqmTFbxUuJ43vUda10y3iqI4mmZ_o-wGLXRI-YQ";

    private GoogledriveClient client;
    private Path rootPath;

    @Before
    public void setUp() throws IOException {
        GoogleCredential credential = new GoogleCredential().setAccessToken(ACCESS_TOKEN);
        Drive wrappedClient = new Drive.Builder(HTTP_TRANSPORT, JSON_FACTORY, credential)
                .setApplicationName("Syncany Test Suite")
                .build();

        client = new GoogledriveClient(wrappedClient);
        rootPath = Paths.get("/test");
        if(client.folderExists(rootPath)) {
            client.delete(rootPath);
        }
        client.createFolder(rootPath);
    }

    @Test
    public void testAbout() throws IOException {
        String name = client.about().getName();
        Assert.assertEquals("Lukas Martinelli", name);
    }

    @Test
    public void testCreateFolder() throws IOException {
        client.createFolder(rootPath.resolve("folder"));

        Assert.assertTrue(client.folderExists(rootPath.resolve("folder")));
    }
}
