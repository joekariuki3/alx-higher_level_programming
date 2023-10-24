#!/usr/bin/node
// script to count how many task a user has completed

const request = require('request');

function getCompleted (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const jsonData = JSON.parse(body);
    const tasks = {};
    for (let i = 0; i < jsonData.length; i++) {
      const userId = jsonData[i].userId;
      const completed = jsonData[i].completed;
      // check if the task is completed
      if (completed) {
        // if key not in tasks add it
        if (!(userId in tasks)) {
          tasks[`${userId}`] = 1;
        } else {
          const value = tasks[`${userId}`] + 1;
          tasks[`${userId}`] = value;
        }
      }
    }
    console.log(tasks);
  });
}

if (process.argv[2]) {
  const url = process.argv[2];
  getCompleted(url);
}
