#!/usr/bin/node
// get a file page

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
