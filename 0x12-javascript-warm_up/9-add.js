#!/usr/bin/node
function addition (a, b) {
  const res = a + b;
  console.log(res);
}

addition(parseInt(process.argv[2]), parseInt(process.argv[3]));
