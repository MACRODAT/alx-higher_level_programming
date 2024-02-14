#!/usr/bin/node
// rev

exports.esrever = function (list) {
  let rlist = [];
  while (list.length > 0) {
    rlist.push(list.pop());
  }
  return rlist;
};
