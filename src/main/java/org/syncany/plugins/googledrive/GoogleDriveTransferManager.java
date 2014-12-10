/*
 * Syncany, www.syncany.org
 * Copyright (C) 2011-2014 Philipp C. Heckel <philipp.heckel@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package org.syncany.plugins.googledrive;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

import org.syncany.config.Config;
import org.syncany.plugins.transfer.AbstractTransferManager;
import org.syncany.plugins.transfer.StorageException;
import org.syncany.plugins.transfer.TransferManager;
import org.syncany.plugins.transfer.files.*;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

/**
 * <p>
 * Implements a {@link TransferManager} based on an Google Drive storage backend for the
 * {@link GoogleDriveTransferPlugin}.
 * <p/>
 * <p>Using a {@link GoogleDriveTransferSettings}, the transfer manager is configured and uses
 * a well defined Samba share and folder to store the Syncany repository data. While repo and
 * master file are stored in the given folder, databases and multichunks are stored
 * in special sub-folders:
 * <p/>
 * <ul>
 * <li>The <tt>databases</tt> folder keeps all the {@link DatabaseRemoteFile}s</li>
 * <li>The <tt>multichunks</tt> folder keeps the actual data within the {@link MultiChunkRemoteFile}s</li>
 * </ul>
 * <p/>
 * <p>All operations are auto-connected, i.e. a connection is automatically
 * established.
 *
 * @author Christian Roth <christian.roth@port17.de>
 */
public class GoogleDriveTransferManager extends AbstractTransferManager {
	private static final Logger logger = Logger.getLogger(GoogleDriveTransferManager.class.getSimpleName());

	private final String path;
	private final String multichunksPath;
	private final String databasesPath;
	private final String actionsPath;
	private final String transactionsPath;
	private final String tempPath;

	private final String authorizationCode;
	private GoogleDriveClient client;

	public GoogleDriveTransferManager(GoogleDriveTransferSettings settings, Config config) {
		super(settings, config);

		this.path = ("/" + settings.path.getPath()).replaceAll("[/]{2,}", "/");
		this.multichunksPath = new File(this.path, "/multichunks/").getPath();
		this.databasesPath = new File(this.path, "/databases/").getPath();
		this.actionsPath = new File(this.path, "/actions/").getPath();
		this.transactionsPath = new File(this.path, "/transactions/").getPath();
		this.tempPath = new File(this.path, "/temporary/").getPath();

		this.authorizationCode = settings.authorizationCode;
	}

	@Override
	public void connect() throws StorageException {
		try {
			this.client = GoogleDriveTransferPlugin.createClient(authorizationCode);
			logger.log(Level.INFO, "Using googledrive account from {0}", new Object[] { this.client.about().getName() });
		}
		catch (IOException e) {
			throw new StorageException("Unable to connect to dropbox", e);
		}
	}

	@Override
	public void disconnect() {
	}



	@Override
	public void init(boolean createIfRequired) throws StorageException {
		connect();

		try {
			if (!testTargetExists() && createIfRequired) {
				this.client.createFolder(this.path);
			}

			this.client.createFolder(this.multichunksPath);
			this.client.createFolder(this.databasesPath);
			this.client.createFolder(this.actionsPath);
			this.client.createFolder(this.transactionsPath);
			this.client.createFolder(this.tempPath);
		}
		catch (IOException e) {
			throw new StorageException("init: Cannot create required directories", e);
		}
		finally {
			disconnect();
		}
	}


	@Override
	public void download(RemoteFile remoteFile, File localFile) throws StorageException {
		throw new NotImplementedException();
//		String remotePath = getRemoteFile(remoteFile);
//
//		if (!remoteFile.getName().equals(".") && !remoteFile.getName().equals("..")) {
//			try {
//				// Download file
//				File tempFile = createTempFile(localFile.getName());
//				OutputStream tempFOS = new FileOutputStream(tempFile);
//
//				if (logger.isLoggable(Level.INFO)) {
//					logger.log(Level.INFO, "Dropbox: Downloading {0} to temp file {1}", new Object[] { remotePath, tempFile });
//				}
//
//				this.client.getFile(remotePath, null, tempFOS);
//
//				tempFOS.close();
//
//				// Move file
//				if (logger.isLoggable(Level.INFO)) {
//					logger.log(Level.INFO, "Dropbox: Renaming temp file {0} to file {1}", new Object[] { tempFile, localFile });
//				}
//
//				localFile.delete();
//				FileUtils.moveFile(tempFile, localFile);
//				tempFile.delete();
//			}
//			catch (DbxException | IOException ex) {
//				logger.log(Level.SEVERE, "Error while downloading file " + remoteFile.getName(), ex);
//				throw new StorageException(ex);
//			}
//		}
	}

	@Override
	public void upload(File localFile, RemoteFile remoteFile) throws StorageException {
		throw new NotImplementedException();
//		String remotePath = getRemoteFile(remoteFile);
//		String tempRemotePath = this.path + "/temp-" + remoteFile.getName();
//
//		try {
//			// Upload to temp file
//			InputStream fileFIS = new FileInputStream(localFile);
//
//			if (logger.isLoggable(Level.INFO)) {
//				logger.log(Level.INFO, "Dropbox: Uploading {0} to temp file {1}", new Object[] { localFile, tempRemotePath });
//			}
//
//			this.client.uploadFile(tempRemotePath, DbxWriteMode.add(), localFile.length(), fileFIS);
//
//			fileFIS.close();
//
//			// Move
//			if (logger.isLoggable(Level.INFO)) {
//				logger.log(Level.INFO, "Dropbox: Renaming temp file {0} to file {1}", new Object[] { tempRemotePath, remotePath });
//			}
//
//			this.client.move(tempRemotePath, remotePath);
//		}
//		catch (DbxException | IOException ex) {
//			logger.log(Level.SEVERE, "Could not upload file " + localFile + " to " + remoteFile.getName(), ex);
//			throw new StorageException(ex);
//		}
	}

	@Override
	public boolean delete(RemoteFile remoteFile) throws StorageException {
		throw new NotImplementedException();
//		String remotePath = getRemoteFile(remoteFile);
//
//		try {
//			this.client.delete(remotePath);
//			return true;
//		}
//		catch (DbxException ex) {
//			logger.log(Level.SEVERE, "Could not delete file " + remoteFile.getName(), ex);
//			throw new StorageException(ex);
//		}
	}

	@Override
	public void move(RemoteFile sourceFile, RemoteFile targetFile) throws StorageException {
		throw new NotImplementedException();
//		String sourceRemotePath = getRemoteFile(sourceFile);
//		String targetRemotePath = getRemoteFile(targetFile);
//
//		try {
//			this.client.move(sourceRemotePath, targetRemotePath);
//		}
//		catch (DbxException e) {
//			logger.log(Level.SEVERE, "Could not rename file " + sourceRemotePath + " to " + targetRemotePath, e);
//			throw new StorageMoveException("Could not rename file " + sourceRemotePath + " to " + targetRemotePath, e);
//		}
	}

	@Override
	public <T extends RemoteFile> Map<String, T> list(Class<T> remoteFileClass) throws StorageException {
		throw new NotImplementedException();
//		try {
//			// List folder
//			String remoteFilePath = getRemoteFilePath(remoteFileClass);
//
//			DbxEntry.WithChildren listing = this.client.getMetadataWithChildren(remoteFilePath);
//
//			// Create RemoteFile objects
//			Map<String, T> remoteFiles = new HashMap<String, T>();
//
//			for (DbxEntry child : listing.children) {
//				try {
//					T remoteFile = RemoteFile.createRemoteFile(child.name, remoteFileClass);
//					remoteFiles.put(child.name, remoteFile);
//				}
//				catch (Exception e) {
//					logger.log(Level.INFO, "Cannot create instance of " + remoteFileClass.getSimpleName() + " for file " + child.name
//							+ "; maybe invalid file name pattern. Ignoring file.");
//				}
//			}
//
//			return remoteFiles;
//		}
//		catch (DbxException ex) {
//			disconnect();
//
//			logger.log(Level.SEVERE, "Unable to list Dropbox directory.", ex);
//			throw new StorageException(ex);
//		}
	}

	private String getRemoteFile(RemoteFile remoteFile) {
		return getRemoteFilePath(remoteFile.getClass()) + "/" + remoteFile.getName();
	}

	private String getRemoteFilePath(Class<? extends RemoteFile> remoteFile) {
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

	@Override
	public boolean testTargetCanWrite() {
		try {
			if (testTargetExists()) {
				String tempRemoteFile = this.path + "/syncany-write-test";
				File tempFile = File.createTempFile("syncany-write-test", "tmp");

				this.client.uploadFile(tempRemoteFile, tempFile);
				this.client.delete(tempRemoteFile);

				tempFile.delete();

				logger.log(Level.INFO, "testTargetCanWrite: Can write, test file created/deleted successfully.");
				return true;
			}
			else {
				logger.log(Level.INFO, "testTargetCanWrite: Can NOT write, target does not exist.");
				return false;
			}
		}
		catch (IOException e) {
			logger.log(Level.INFO, "testTargetCanWrite: Can NOT write to target.", e);
			return false;
		}
	}

	@Override
	public boolean testTargetExists() {
		try {
			return this.client.folderExists(this.path);
		}
		catch (IOException e) {
			logger.log(Level.WARNING, "testTargetExists: Target does NOT exist, error occurred.", e);
			return false;
		}
	}

	@Override
	public boolean testTargetCanCreate() {
		String parentPath = Paths.get(this.path).getParent().toString();

		try {
			if(this.client.folderExists(parentPath)) {
				logger.log(Level.INFO, "testTargetCanCreate: Can create target at " + parentPath);
				return true;
			} else {
				logger.log(Level.INFO, "testTargetCanCreate: Can NOT create target (parent does not exist)");
				return false;
			}
		}
		catch (IOException e) {
			logger.log(Level.INFO, "testTargetCanCreate: Can NOT create target at " + parentPath, e);
			return false;
		}
	}

	@Override
	public boolean testRepoFileExists() {
		try {
			String repoFilePath = getRemoteFile(new SyncanyRemoteFile());

			if(client.fileExists(repoFilePath)) {
				logger.log(Level.INFO, "testRepoFileExists: Repo file exists at " + repoFilePath);
				return true;
			}
			else {
				logger.log(Level.INFO, "testRepoFileExists: Repo file DOES NOT exist at " + repoFilePath);
				return false;
			}
		}
		catch (Exception e) {
			logger.log(Level.INFO, "testRepoFileExists: Exception when trying to check repo file existence.", e);
			return false;
		}
	}
}
