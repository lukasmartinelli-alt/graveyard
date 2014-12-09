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

import org.syncany.plugins.transfer.Encrypted;
import org.syncany.plugins.transfer.Setup;
import org.syncany.plugins.transfer.TransferPluginOptionCallback;
import org.syncany.plugins.transfer.TransferSettings;

import com.google.api.services.drive.Drive;
import org.simpleframework.xml.Element;

import java.io.File;
import java.io.IOException;

public class GoogleDriveTransferSettings extends TransferSettings {
	@Element(name = "authorizationCode", required = true)
	@Setup(order = 1, sensitive = true, singular = true, description = "Access token", callback = GoogleDriveAuthPluginOptionCallback.class)
	@Encrypted
	public String authorizationCode;

	@Element(name = "path", required = true)
	@Setup(order = 2, description = "Path relative to syncany's app root")
	public File path;

	public static class GoogleDriveAuthPluginOptionCallback implements TransferPluginOptionCallback {
		@Override
		public String preQueryCallback() {
			String authorizeUrl = GoogleDriveTransferPlugin.getAuthorizationUrl();
			return String.format(
				      "\n"
					+ "The Google Drive plugin needs to obtain an access token from Google\n"
					+ "to read and write to your Google Drive. Please follow the instructions\n"
					+ "on the following site to authorize Syncany:\n"
					+ "\n"
					+ "    %s\n", authorizeUrl);
		}

		@Override
		public String postQueryCallback(String optionValue) {
			try {
				Drive client = GoogleDriveTransferPlugin.createClient(optionValue);
				return String.format("\nSuccessfully linked with %s's account!\n", client.about().get().execute().getName());
			}
			catch (IOException e) {
				throw new RuntimeException("Error requesting googledrive data: " + e.getMessage());
			}
		}
	}
}
