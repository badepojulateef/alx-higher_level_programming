#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = Object.entries(dict)
  .reduce(function (acc, [userId, occur]) {
    const ids = acc[occur] || [];
    return {
      ...acc,
      [occur]: [...ids, userId]
    };
  }, {});

console.log(newDict);
