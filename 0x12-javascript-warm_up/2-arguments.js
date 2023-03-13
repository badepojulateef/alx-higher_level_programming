#!/usr/bin/node

const noOfArguments = process.argv.slice(2).length;

if (noOfArguments === 0) {
  console.log('No argument');
} else if (noOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
