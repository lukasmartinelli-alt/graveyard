var express = require('express');
var router = express.Router();

router.route('/students')
    .get(function(req, res) {
        return [{ name: "sALI" }];
    });

module.exports = router;
