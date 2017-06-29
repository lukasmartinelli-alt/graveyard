#!/usr/bin/env node
'use strict';
/* eslint-disable no-console */

const util = require('util');
const program = require('commander');
const fs = require('fs');
const mkdirp = require('mkdirp');
const path = require('path');
const exec = require('child_process').exec;
const tilelive = require("tilelive");
const walk = require('walk');

require('tilelive-file').registerProtocols(tilelive);
require('mbtiles').registerProtocols(tilelive);

program
  .option('-i, --input [file]', 'GeoJSON feature collection')
  .option('-d, --output-dir [dir]', 'Directrory to store tiles in')
  .parse(process.argv);

function copyTiles(mbtilesPath, outputDir, cb) {
	const source = "mbtiles://" + path.resolve(mbtilesPath);
	const target = "file://" + path.resolve(outputDir);
  tilelive.copy(source, target, {
    type: 'scanline',
  }, function(err) {
    if (err) throw err;
		cb();
  });
}

function fixTiles(outputDir) {
  const walker = walk.walk(outputDir, {

	});
  walker.on("file", function (root, fileStats, next) {
		if(path.extname(fileStats.name) === '.png') {
			const newFile = path.join(root, path.basename(fileStats.name, '.png') + '.pbf.gz');
			fs.renameSync(path.join(root, fileStats.name), newFile);
			//TODO: No subprocessing required
			exec(['gunzip', newFile].join(' '), function(err) {
				if(err) throw err;
			});
		}
		next();
  });
}

if (program.input && program.outputDir) {
	mkdirp.sync(program.outputDir);
  const collection = JSON.parse(fs.readFileSync(program.input));
	const mbtilesPath = path.join(program.outputDir, 'tiles.mbtiles');
	exec(['tippecanoe -zg -o', mbtilesPath, program.input].join(' '), function(err) {
		if(err) throw err;
		copyTiles(mbtilesPath, program.outputDir, function(err) {
			fixTiles(program.outputDir);
		});
	});
} else {
  program.outputHelp();
}
