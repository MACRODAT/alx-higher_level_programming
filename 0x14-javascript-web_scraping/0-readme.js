#!/usr/bin/node
// A script read files

const fs = require('fs');

function readfs (fp) {
  fs.readFile(fp, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

readfs(process.argv[2]);
