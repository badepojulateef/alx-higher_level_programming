#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function fact (n, result = 1) {
  if (Number.isNaN(arg)) {
    return result;
  }
  if (n < 2) {
    return result;
  }
  return fact(n - 1, n * result);
}

console.log(fact(arg));
