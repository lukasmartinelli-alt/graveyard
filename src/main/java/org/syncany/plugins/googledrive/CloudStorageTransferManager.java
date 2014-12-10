package org.syncany.plugins.googledrive;

import org.syncany.config.Config;
import org.syncany.plugins.transfer.AbstractTransferManager;
import org.syncany.plugins.transfer.StorageException;
import org.syncany.plugins.transfer.TransferSettings;
import org.syncany.plugins.transfer.files.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * <p>
 * A {@link org.syncany.plugins.transfer.TransferManager} base class that is well suited for
 * cloud storage plugins.
 * <p/>
 * <p>
 *     The {@link org.syncany.plugins.googledrive.CloudStorageTransferManager} stores the different
 *     files in different subfolders.
 * </p>
 */
public abstract class CloudStorageTransferManager extends AbstractTransferManager {
    private static final Logger logger = Logger.getLogger(CloudStorageTransferManager.class.getSimpleName());

    private final Path path;
    private final Path multichunksPath;
    private final Path databasesPath;
    private final Path actionsPath;
    private final Path transactionsPath;
    private final Path tempPath;

    public CloudStorageTransferManager(TransferSettings settings, Config config, String path) {
        super(settings, config);

        this.path = Paths.get(path);
        this.multichunksPath = Paths.get(path, "/multichunks/");
        this.databasesPath = Paths.get(path, "/databases/");
        this.actionsPath = Paths.get(path, "/actions/");
        this.transactionsPath = Paths.get(path, "/transactions/");
        this.tempPath = Paths.get(path, "/temporary/");
    }

    public abstract boolean folderExists(Path path) throws IOException;

    public abstract boolean fileExists(Path repoRemotePath);

    public abstract void createFolder(Path tempPath) throws IOException;

    @Override
    public void init(boolean createIfRequired) throws StorageException {
        connect();

        try {
            if (!testTargetExists() && createIfRequired) {
                createFolder(this.path);
            }

            createFolder(this.multichunksPath);
            createFolder(this.databasesPath);
            createFolder(this.actionsPath);
            createFolder(this.transactionsPath);
            createFolder(this.tempPath);
        }
        catch (Exception e) {
            throw new StorageException("init: Cannot create required directories", e);
        }
        finally {
            disconnect();
        }
    }

    @Override
    public boolean testTargetExists() {
        try {
            return folderExists(this.path);
        }
        catch (Exception e) {
            logger.log(Level.WARNING, "testTargetExists: Target does NOT exist, error occurred.", e);
            return false;
        }
    }

    @Override
    public boolean testTargetCanWrite() throws StorageException {
        try {
            if (testTargetExists()) {
                TempRemoteFile tempRemoteFile = RemoteFile.createRemoteFile("sync-write-test", TempRemoteFile.class);
                File tempLocalFile = File.createTempFile("syncany-write-test", "tmp");

                upload(tempLocalFile, tempRemoteFile);
                delete(tempRemoteFile);

                tempLocalFile.delete();

                logger.log(Level.INFO, "testTargetCanWrite: Can write, test file created/deleted successfully.");
                return true;
            }
            else {
                logger.log(Level.INFO, "testTargetCanWrite: Can NOT write, target does not exist.");
                return false;
            }
        }
        catch (Exception e) {
            logger.log(Level.INFO, "testTargetCanWrite: Can NOT write to target.", e);
            return false;
        }
    }

    @Override
    public boolean testTargetCanCreate() {
        Path parentPath = this.path.getParent();

        try {
            if(folderExists(parentPath)) {
                logger.log(Level.INFO, "testTargetCanCreate: Can create target at " + parentPath);
                return true;
            } else {
                logger.log(Level.INFO, "testTargetCanCreate: Can NOT create target (parent does not exist)");
                return false;
            }
        }
        catch (Exception e) {
            logger.log(Level.INFO, "testTargetCanCreate: Can NOT create target at " + parentPath, e);
            return false;
        }
    }

    @Override
    public boolean testRepoFileExists() {
        try {
            Path repoRemotePath = getRemoteFilePath(new SyncanyRemoteFile());

            if(fileExists(repoRemotePath)) {
                logger.log(Level.INFO, "testRepoFileExists: Repo file exists at " + repoRemotePath);
                return true;
            }
            else {
                logger.log(Level.INFO, "testRepoFileExists: Repo file DOES NOT exist at " + repoRemotePath);
                return false;
            }
        }
        catch (Exception e) {
            logger.log(Level.INFO, "testRepoFileExists: Exception when trying to check repo file existence.", e);
            return false;
        }
    }

    protected Path getRemoteFilePath(RemoteFile remoteFile) {
        return getRemoteFileSubfolder(remoteFile.getClass())
                .resolve(Paths.get(remoteFile.getName()));
    }

    protected Path getRemoteFileSubfolder(Class<? extends RemoteFile> remoteFile) {
        if (remoteFile.equals(MultichunkRemoteFile.class)) {
            return multichunksPath;
        }
        else if (remoteFile.equals(DatabaseRemoteFile.class)) {
            return databasesPath;
        }
        else if (remoteFile.equals(ActionRemoteFile.class)) {
            return actionsPath;
        }
        else if (remoteFile.equals(TransactionRemoteFile.class)) {
            return transactionsPath;
        }
        else if (remoteFile.equals(TempRemoteFile.class)) {
            return tempPath;
        }
        else {
            return path;
        }
    }
}

