#!/usr/bin/node

const request = require('request');

const host = process.argv[2];

request(host, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', res.statusCode);
});
