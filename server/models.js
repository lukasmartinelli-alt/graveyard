var mongoose = require('mongoose');

module.exports.Student = mongoose.Model('Student', {
    firstName: String,
    lastName: String,
    fieldOfStudy: String,
    knownFrom: String,
    interests: String,
    mail: String,
    remarks: String,
    birthday: Date
});
