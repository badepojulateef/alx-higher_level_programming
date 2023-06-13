#!/usr/bin/node
// Script that computes and prints a factorial

const { argv } = require('node:process');

function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

console.log(factorial(Number(argv[2])));
