#!/usr/bin/node
// nbr of occurrences in lst

exports.nbOccurences = function (list, searchElement) {
  return list.filter((value) => (value === searchElement)).length;
};
