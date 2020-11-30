// Defining model for top summaries

const { Model } = require('objection');

class topSummariesModel extends Model {
  static get tableName() {
    return 'top_summaries_view';
  }
  static get idColumn() {
    return 'summary_id';
  }
}

module.exports = {
    topSummariesModel
};