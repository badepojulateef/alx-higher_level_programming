#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduce(function (acc, element) {
    return [element].concat(acc);
  }, []);
};
