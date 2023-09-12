#!/usr/bin/node
// funtion to convert from base to to other bases

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
