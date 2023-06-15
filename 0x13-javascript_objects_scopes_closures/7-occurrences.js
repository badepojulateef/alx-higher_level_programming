#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      counter += 1;
    }
    i += 1;
  }
  return counter;
};
