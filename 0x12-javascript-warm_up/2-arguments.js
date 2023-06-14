#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed"


const noOfArgs = process.argv.slice(2).length;

if (noOfArgs === 0) {
  console.log('No argument');
} else if (noOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
