#!/usr/bin/node

const args = process.argv.slice(2);

function func (a) {
  if (args.length < 2) {
    return 0;
  } else {
    const integers = args.map(Number);
    const sortedIntegers = integers.sort((a, b) => b - a);
    return sortedIntegers[1];
  }
}

console.log(func(args));
