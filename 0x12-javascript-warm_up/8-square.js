#!/usr/bin/node
// Script that prints a square

const { argv } = require('node:process');

const size = parseInt(argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i += 1) {
    let row = '';
    for (let j = 0; j < size; j += 1) {
      row += 'X';
    }
    console.log(row);
  }
}
