var mongoose = require('mongoose');

module.exports.Student = mongoose.Model('Student', {
    firstname: String,
    lastname: String,
    mail: String,
    major: String,
    description: String,
});
