package org.syncany.plugins.googledrive;

import org.junit.Test;
import org.syncany.config.Config;
import org.syncany.plugins.transfer.StorageException;

import java.io.IOException;
import java.nio.file.Paths;

import static org.mockito.Mockito.*;

public class GoogledriveTransferManagerTest {
    @Test
    public void testInit() throws IOException, StorageException {
        GoogledriveTransferSettings settings = mock(GoogledriveTransferSettings.class);
        when(settings.getPath()).thenReturn(new java.io.File("testRepo"));
        Config config = mock(Config.class);
        GoogledriveClient client = mock(GoogledriveClient.class);
        when(client.about().getName()).thenReturn("Syncany User");
        GoogledriveTransferManager transferManager = new GoogledriveTransferManager(settings, config, client);

        transferManager.init(true);

        verify(client).createFolder(Paths.get("testRepo"));
        verify(client).createFolder(Paths.get("testRepo/multichunks"));
        verify(client).createFolder(Paths.get("testRepo/databases"));
        verify(client).createFolder(Paths.get("testRepo/actions"));
        verify(client).createFolder(Paths.get("testRepo/transactions"));
        verify(client).createFolder(Paths.get("testRepo/temporary"));
    }
}
