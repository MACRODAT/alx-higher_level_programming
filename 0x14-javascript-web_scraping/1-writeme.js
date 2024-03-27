#!/usr/bin/node
// A script that reads and prints the content of a file

const fl = process.argv[2];
const fs = require('fs');
const data = process.argv[3];

fs.writeFile(fl, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
