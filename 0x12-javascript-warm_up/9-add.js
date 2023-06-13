#!/usr/bin/node
// Script that prints the addition of 2 integers

const { argv } = process;
const arg1 = parseInt(argv[2]);
const arg2 = parseInt(argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(arg1, arg2));
