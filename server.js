var express = require('express');
var mongoose = require('mongoose');
var app = express();
var bodyParser = require('body-parser');
var router = require('./server/routes.js');

mongoose.connect('mongodb://localhost/talentpool');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(express.static(__dirname + '/client'));
app.use('/api', router);
app.listen(process.env.PORT || 3000);
