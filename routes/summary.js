var express = require('express');
var router = express.Router();
const {spawn} = require('child_process');

// Require controller modules.
let summarySubmissionController = require('../controllers/summarySubmissionController');
let recordsController = require('../controllers/recordsController');

// GET summary homepage
router.get('/', summarySubmissionController.index);

// request for new user submitted summaries
router.get('/submit',summarySubmissionController.submitSummaryGet);
router.post('/submit',summarySubmissionController.submitSummaryPost);

// GET request for summary records
router.get('/records',recordsController.recordsGet)

module.exports = router;