#!/usr/bin/node
function addition (a, b) {
  const c = a + b;
  console.log(c);
}

addition(Number(process.argv[2]), Number(process.argv[3]));
