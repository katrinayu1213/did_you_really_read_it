// Load validator
const { body, validationResult } = require('express-validator');

// Load functions
let iotools = require('../iotools');

// uuid generator
const { v4: uuidv4 } = require('uuid');

// models
const { userSummaryModel } = require('../models/userSummaryModel');

// summary controller

exports.index = async function (req, res) {
    // Read all rows from the db.
    const allSummaries = await userSummaryModel.query()
        .distinct('summary_id');
    let indexInfo = {
        title: "Summary Project Demo",
        summaryCount: allSummaries.length.toLocaleString()
    }
    console.log(indexInfo);
    res.render('index', indexInfo);
};

exports.submitSummaryGet = async function (req, res) {
    let pageInfo = {
        title: "Read and submit summary"
    }
    res.render('submitSummary', pageInfo);
};

exports.submitSummaryPost = [
    body('userSummary', 'Error with summary').trim(),

    // Process request after validation and sanitization.
    async function (req, res) {

        // Extract the validation errors from a request.
        const errors = validationResult(req);

        if (!errors.isEmpty()) {
            // There are errors. Render the form again with sanitized values/error messages.
            res.render('submitSummary', {
                title: 'Submit summary: Fix Errors',userSummary: req.body.userSummary, errors: errors.array()
            });
            return;
        }
        else {
            const spawn = require("child_process").spawn;
            const pythonProcess = spawn(
                'python',
                ["./python/lsa_with_news_corpus.py", req.body.userSummary]);
            pythonProcess.stdout.on('data', function(data) { 
                //res.send(data.toString()); 
                console.log(data.toString());
                addSummary(req.body.userSummary,data.toString());
                res.redirect('/summaries/records');
            } ); 

            async function addSummary(summary,lsa) {
                let newId = uuidv4();
                let newSummary = await userSummaryModel.query().insert({
                    summary_id: newId,
                    user_id: '1b5d7975-a380-4263-9beb-5efd480b34f3',
                    reference_text_id: '1',
                    summary_text: summary,
                    word_count: iotools.wordCount(summary),
                    lsa_similarity: lsa,
                    date_added: await iotools.currentDate()
                });
            }
        }
    }
];