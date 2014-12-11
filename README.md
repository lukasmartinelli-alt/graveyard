# Syncany Google Drive Plugin [![Build Status](https://travis-ci.org/lukasmartinelli/syncany-plugin-googledrive.svg)](https://travis-ci.org/lukasmartinelli/syncany-plugin-googledrive)

The Google Drive Plugin uses an App folder inside your Google Drive to store all repo data.

## Build

Build the plugin and install it to your local syncany installation.

```
gradle clean pluginJar
sy plugin remove googledrive
sy plugin install build/libs/*.jar
```

Run the tests.

```
gradle test
```

## Development

For plugin development, please refer to the [plugin development wiki page](https://github.com/syncany/syncany/wiki/Plugin-development).
