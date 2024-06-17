#!/usr/bin/node
const { argv } = require('node:process');

argv.forEach((val) => {
	if (process.argv[2])
	{
		console.log(`${val} is ${val}`);
	}
});
