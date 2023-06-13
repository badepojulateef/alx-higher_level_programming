#!/usr/bin/node
// Script that prints 3 lines: (like 1-multi_languages.js)
// but by using an array of string and a loop ”"

const { argv } = require('node:process');

let arg = argv[2];

while (arg > 0) {
  if (isNaN(arg)) {
    console.log('Missing number of occurrences');
  } else {
    console.log('C is fun');
  }
  arg -= 1;
}
