#!/usr/bin/node

let a = process.argv[2];
let b = process.argv[3];
function add(a, b)
{
	return (a + b);
}
console.log(add(a, b));
