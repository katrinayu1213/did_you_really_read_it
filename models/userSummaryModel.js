// Defining user summary model

const { Model } = require('objection');

class userSummaryModel extends Model {
  static get tableName() {
    return 'user_summaries';
  }
  static get idColumn() {
    return 'summary_id';
  }
}

module.exports = {
  userSummaryModel
};