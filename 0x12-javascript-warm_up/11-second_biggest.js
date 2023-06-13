#!/usr/bin/node

const { argv } = require('process');

const args = argv.slice(2);

function func (a) {
  if (args.length < 2) {
    return 0;
  } else {
    const ints = args.map(Number);
    const sortedInts = ints.sort((a, b) => b - a);
    return sortedInts[1];
  }
}

console.log(func(args));
