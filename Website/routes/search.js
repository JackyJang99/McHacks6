var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    var id = req.query.patientId;
    res.sendFile("C:/Users/Rui Ze/WebstormProjects/McHacks/routes/pages/" + id + ".html"); // send whatever content, maybe the whole html?
});

module.exports = router;