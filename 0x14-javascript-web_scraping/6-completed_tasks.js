#!/usr/bin/node
// tasks completed

const args = process.argv;
let url_ = args[2];
let request = require('request');
request(url_, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let todos = JSON.parse(body);
    let dash = {};
    for (let i = 0; i < todos.length; i++) {
      let stat = (todos[i]['completed']);
      let user_id = todos[i]['userId'].toString();
      if (stat) {
        if (dash[user_id]) {
          dash[user_id]++;
        } else {
          dash[user_id] = 1;
        }
      }
    }
    console.log(dash);
  }
});
