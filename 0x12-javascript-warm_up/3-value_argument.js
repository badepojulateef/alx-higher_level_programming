#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed"

const { argv } = require('node:process');

console.log(argv[2] || 'No argument');
