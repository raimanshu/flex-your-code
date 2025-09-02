
// Method 5: Binet's Formula (Closed-form expression)

var fib = function(n) {
    const sqrt5 = Math.sqrt(5);
    const fibN = Math.pow((1 + sqrt5) / 2, n) - Math.pow((1 - sqrt5) / 2, n);
    return Math.round(fibN / sqrt5);
};

input = 4;
console.log(fib(input)); // Output: 3