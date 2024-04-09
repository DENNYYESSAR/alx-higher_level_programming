#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (number) {
    if (number === 0) {
      return '';
    } else {
      return convertToBase(Math.floor(number / base)) + (number % base).toString(base).toUpperCase();
    }
  };
};
