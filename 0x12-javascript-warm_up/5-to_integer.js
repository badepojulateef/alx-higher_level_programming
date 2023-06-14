#!/usr/bin/node
// Script that prints two arguments passed to it, in the following format: “ is ”"

const arg = parseInt(process.argv[2]);

console.log(Number.isInteger(arg) ? `My number: ${arg}` : 'Not a number');
