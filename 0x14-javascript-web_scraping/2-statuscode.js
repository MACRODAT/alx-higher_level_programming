#!/usr/bin/node
// get req status

const url_ = process.argv[2];
const request = require('request');
request(url_, function (error, response, body) {
  if (error) {
    console.log(error); // Print the error if one occurred
  } else {
    console.log('code:', response && response.statusCode);
  }
});
