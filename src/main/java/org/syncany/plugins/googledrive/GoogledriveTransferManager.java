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

import org.apache.commons.io.FileUtils;
import org.syncany.config.Config;
import org.syncany.plugins.transfer.StorageException;
import org.syncany.plugins.transfer.StorageMoveException;
import org.syncany.plugins.transfer.TransferManager;
import org.syncany.plugins.transfer.files.*;

import javax.naming.OperationNotSupportedException;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * <p>
 * Implements a {@link TransferManager} based on an Google Drive storage backend for the
 * {@link GoogledriveTransferPlugin}.
 * <p/>
 * <p>Using a {@link GoogledriveTransferSettings}, the transfer manager is configured and uses
 * a well defined Samba share and folder to store the Syncany repository data. While repo and
 * master file are stored in the given folder, databases and multichunks are stored
 * in special sub-folders.
 * <p/>
 * <p>All operations are auto-connected, i.e. a connection is automatically
 * established.
 *
 * @author Christian Roth <christian.roth@port17.de>
 */
public class GoogledriveTransferManager extends CloudStorageTransferManager {
	private static final Logger logger = Logger.getLogger(GoogledriveTransferManager.class.getSimpleName());

	private final String accessToken;

	private GoogledriveClient client;

	public GoogledriveTransferManager(GoogledriveTransferSettings settings, Config config) {
		super(settings, config, settings.path.getPath());
		this.accessToken = settings.accessToken;
	}

	@Override
	public void connect() throws StorageException {
		try {
			this.client = GoogledriveTransferPlugin.createClient(accessToken);
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
	public void download(RemoteFile remoteFile, File localFile) throws StorageException {
		Path remotePath = getRemoteFilePath(remoteFile);

		if (!remoteFile.getName().equals(".") && !remoteFile.getName().equals("..")) {
			try {
				File tempFile = createTempFile(localFile.getName());
				OutputStream tempLocalOutputStream = new FileOutputStream(tempFile);

				if (logger.isLoggable(Level.INFO)) {
					logger.log(Level.INFO, "Dropbox: Downloading {0} to temp file {1}", new Object[] { remotePath, tempFile });
				}

				this.client.downloadFile(remotePath, tempLocalOutputStream);
				tempLocalOutputStream.close();

				// Move file
				if (logger.isLoggable(Level.INFO)) {
					logger.log(Level.INFO, "Dropbox: Renaming temp file {0} to file {1}", new Object[] { tempFile, localFile });
				}

				localFile.delete();
				FileUtils.moveFile(tempFile, localFile);
				tempFile.delete();
			}
			catch (IOException ex) {
				logger.log(Level.SEVERE, "Error while downloading file " + remoteFile.getName(), ex);
				throw new StorageException(ex);
			}
		}
	}

	@Override
	public void upload(File localFile, RemoteFile remoteFile) throws StorageException {
		Path remotePath = getRemoteFilePath(remoteFile);

		try {
			if (logger.isLoggable(Level.INFO)) {
				logger.log(Level.INFO, "GoogleDrive: Uploading {0} to temp file {1}", new Object[] { localFile, remotePath });
			}
			this.client.uploadFile(remotePath, localFile);
		}
		catch (IOException ex) {
			logger.log(Level.SEVERE, "Could not upload file " + localFile + " to " + remoteFile.getName(), ex);
			throw new StorageException(ex);
		}
	}

	@Override
	public boolean delete(RemoteFile remoteFile) throws StorageException {
		Path remotePath = getRemoteFilePath(remoteFile);

		try {
			this.client.delete(remotePath);
			return true;
		}
		catch (IOException ex) {
			logger.log(Level.SEVERE, "Could not delete file " + remoteFile.getName(), ex);
			throw new StorageException(ex);
		}
	}

	@Override
	public void move(RemoteFile sourceFile, RemoteFile targetFile) throws StorageException {
		Path sourceRemotePath = getRemoteFilePath(sourceFile);
		Path targetRemotePath = getRemoteFilePath(targetFile);

		try {
			this.client.move(sourceRemotePath, targetRemotePath);
		}
		catch (IOException e) {
			logger.log(Level.SEVERE, "Could not rename file " + sourceRemotePath + " to " + targetRemotePath, e);
			throw new StorageMoveException("Could not rename file " + sourceRemotePath + " to " + targetRemotePath, e);
		}
		catch (OperationNotSupportedException e) {
			logger.log(Level.SEVERE, "Renaming a folder " + sourceRemotePath + " to " + targetRemotePath + " is not supported in Google Drive", e);
			throw new StorageMoveException("Could not rename file " + sourceRemotePath + " to " + targetRemotePath, e);
		}
	}

	@Override
	public <T extends RemoteFile> Map<String, T> list(Class<T> remoteFileClass) throws StorageException {
		try {
			Path remoteFilePath = getRemoteFileSubfolder(remoteFileClass);
			Map<String, T> remoteFiles = new HashMap<>();

			for (com.google.api.services.drive.model.File child : this.client.list(remoteFilePath)) {
				try {
					T remoteFile = RemoteFile.createRemoteFile(child.getTitle(), remoteFileClass);
					remoteFiles.put(child.getTitle(), remoteFile);
				}
				catch (Exception e) {
					logger.log(Level.INFO, "Cannot create instance of " + remoteFileClass.getSimpleName() + " for file " + child.getTitle()
							+ "; maybe invalid file name pattern. Ignoring file.");
				}
			}
			return remoteFiles;
		}
		catch (IOException ex) {
			disconnect();

			logger.log(Level.SEVERE, "Unable to list Google Drive directory.", ex);
			throw new StorageException(ex);
		}
	}

	@Override
	public boolean folderExists(Path path) throws IOException {
		return client.folderExists(path);
	}

	@Override
	public boolean fileExists(Path repoRemotePath) {
		return client.fileExists(repoRemotePath);
	}

	@Override
	public void createFolder(Path tempPath) throws IOException {
		client.createFolder(tempPath);

	}
}
