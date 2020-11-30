// uuid generator
const { v4: uuidv4 } = require('uuid');

module.exports = {
    currentDate: async function () {
        let date_ob = new Date();
        let date = ("0" + date_ob.getDate()).slice(-2);
        let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
        let year = date_ob.getFullYear();
        return(year + '-' + month + '-' + date);
    },
    sleep: function (milliseconds) {
        const date = Date.now();
        let currentDate = null;
        do {
            currentDate = Date.now();
        } while (currentDate - date < milliseconds);
    },
    wordCount: function (str) { 
        return str.split(" ").length;
    }
  };