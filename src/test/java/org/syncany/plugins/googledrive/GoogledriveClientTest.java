package org.syncany.plugins.googledrive;

import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.drive.Drive;
import junit.framework.Assert;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.Console;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class GoogledriveClientTest {
    private static final HttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    private static final JsonFactory JSON_FACTORY = new JacksonFactory();
    private static final String ACCESS_TOKEN = "ya29.2ADwZer2iUjkFRV4wKkwSwP6aFZUpRwrDCeRlr1Q-yqjHOHLavko5J6XNJwewsciFao7w8oyltuAHg";

    private GoogledriveClient client;
    private Path rootPath;

    /*
    private void printAccessToken() throws IOException {
        String authorizationToken = "4/WagjLkw6fFDruMBwJE27aiwFfZYgbn-h156Y80G9AK4.8nTWns_4T6ITYFZr95uygvW5-uxrlAI";
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
