#!/usr/bin/node
const { list } = require('./100-data');
// console.log(list);
const newList = list.map(function (item, idx) {
  return item * idx;
});
console.log(list);
console.log(newList);
