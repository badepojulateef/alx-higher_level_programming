#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed"

const { argv } = require('node:process');

const noOfArgs = argv.slice(2).length;

if (noOfArgs === 0) {
  console.log('No argument');
} else if (noOfArgs === 1) {
  console.log('Argument found');
} else if (noOfArgs >= 2) {
  console.log('Arguments found');
}
