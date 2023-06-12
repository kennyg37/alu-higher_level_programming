#!/usr/bin/node
anyArg = process.argv[2];
if (anyArg === undefined) {
	console.log("No argument");
} else {
	console.log(anyArg);
}
