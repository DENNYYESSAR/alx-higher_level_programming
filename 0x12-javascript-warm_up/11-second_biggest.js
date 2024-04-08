#!/usr/bin/node

function secondLargest (arr) {
  if (arr.length <= 1) {
    return 0;
  }

  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      secondMax = max;
      max = arr[i];
    } else if (arr[i] > secondMax && arr[i] < max) {
      secondMax = arr[i];
    }
  }

  return secondMax;
}

const args = process.argv.slice(2).map(Number);
console.log(secondLargest(args));
