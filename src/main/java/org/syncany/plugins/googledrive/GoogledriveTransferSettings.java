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

import com.google.api.client.googleapis.auth.oauth2.GoogleTokenResponse;
import org.syncany.plugins.transfer.*;
import org.simpleframework.xml.Element;

import java.io.File;
import java.io.IOException;

public class GoogledriveTransferSettings extends TransferSettings {
	@Element(name = "accessToken", required = true)
	@Setup(order = 1, sensitive = true, singular = true, description = "Access token", callback = GoogleDriveAuthPluginOptionCallback.class, converter = GoogledriveAuthPluginOptionConverter.class)
	@Encrypted
	public String accessToken;

	@Element(name = "path", required = true)
	@Setup(order = 2, description = "Path relative to Google Drive application root")
	public File path;

	public static class GoogleDriveAuthPluginOptionCallback implements TransferPluginOptionCallback {
		@Override
		public String preQueryCallback() {
			String authorizeUrl = GoogledriveTransferPlugin.getAuthorizationUrl();
			return String.format(
				      "\n"
					+ "The Google Drive plugin needs to obtain an access token from Google\n"
					+ "to read and write to your Google Drive. Please follow the instructions\n"
					+ "on the following site to authorize Syncany:\n"
					+ "\n"
					+ "    %s\n", authorizeUrl);
		}

		@Override
		public String postQueryCallback(String accessToken) {
			try {
				GoogledriveClient client = GoogledriveTransferPlugin.createClient(accessToken);
				return String.format("\nSuccessfully linked with %s's account!\n", client.about().getName());
			}
			catch (IOException e) {
				throw new RuntimeException("Error requesting googledrive data: " + e.getMessage());
			}
		}
	}

	public static class GoogledriveAuthPluginOptionConverter implements TransferPluginOptionConverter {
		@Override
		public String convert(String input) {
			try {
				GoogleTokenResponse response = GoogledriveTransferPlugin.FLOW
						.newTokenRequest(input)
						.setRedirectUri(GoogledriveTransferPlugin.REDIRECT_URI)
						.execute();
				return response.getAccessToken();
			}
			catch (IOException e) {
				throw new RuntimeException("Unable to extract oauth token: " + e.getMessage());
			}
		}
	}
}
