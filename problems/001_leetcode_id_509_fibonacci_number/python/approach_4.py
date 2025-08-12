# Method 4: Dynamic Programming with Memoization

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

input = 4
print(fib(input))  # Output: 3