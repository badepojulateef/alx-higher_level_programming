#!/usr/bin/node
const { list } = require('./100-data');

const computedList = list.map(function (item, idx) {
  return item * idx;
});

console.log(list);
console.log(computedList);
