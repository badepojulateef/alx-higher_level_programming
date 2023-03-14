#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i += 1) {
    if (list[i] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
