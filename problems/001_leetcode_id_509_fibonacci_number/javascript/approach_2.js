
// Method 2: Recursive Approach

var fib = function(n) {
    if(n == 0) return 0
    if(n == 1) return 1
    return fib(n-1) + fib(n-2)
};

input = 4;
console.log(fib(input)); // Output: 3