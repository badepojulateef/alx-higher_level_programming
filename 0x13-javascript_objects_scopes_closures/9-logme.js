#!/usr/bin/node

let argCounter = 0;
exports.logMe = function (item) {
  console.log(`${argCounter}: ${item}`);
  argCounter += 1;
};
