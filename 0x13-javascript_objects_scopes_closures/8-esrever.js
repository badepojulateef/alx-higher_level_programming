#!/usr/bin/node

function reducerFunction (acc, element) {
  return [element].concat(acc);
}

exports.esrever = function (list) {
  return list.reduce(reducerFunction, []);
};
