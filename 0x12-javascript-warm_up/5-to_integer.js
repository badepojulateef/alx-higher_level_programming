#!/usr/bin/node
const arg = parseInt(process.argv[2]);
console.log(Number.isInteger(arg) ? `My number: ${arg}` : 'Not a number');
