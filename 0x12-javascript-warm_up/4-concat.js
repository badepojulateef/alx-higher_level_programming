#!/usr/bin/node
// Script that prints two arguments passed to it, in the following format: “ is ”"

const { argv } = require('node:process');

console.log(argv[2] + ' is ' + argv[3]);
