#!/usr/bin/node
const factorial = (num) => {
	if (isNaN(num)) {
		return 1;
	} else if (num === 0) {
		return 1;
	} else {
		return num * factorial(num - 1);
	}
};
const input = parseInt(process.argv[2], 10);
console.log(factorial(input));

