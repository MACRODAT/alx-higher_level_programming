#!/usr/bin/node
// number of movies

const args = process.argv;
let reqURL = args[2];
let request = require('request');
request(reqURL, function (err, response, body) {
  if (err) {
    console.error(err);
    let jso = JSON.parse(body);
    let results = jso['results'];
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      let chars = (results[i]['characters']);
      for (let j = 0; j < chars.length; j++) {
        let check18 = chars[j].endsWith('18/');
        if (check18) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
