// models
const { topSummariesModel } = require('../models/topSummariesModel');

// records
exports.recordsGet = async function (req, res) {
    const topSummaries = await topSummariesModel.query();
    let pageInfo = {
        title: "Highest and Lowest similarity scores"
    }
    res.render('records', {pageInfo: pageInfo, topSummaries: topSummaries});
};