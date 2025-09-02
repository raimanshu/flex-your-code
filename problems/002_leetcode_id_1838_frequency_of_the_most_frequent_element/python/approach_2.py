
# Method 2: Recursive Approach

def fib(n): 
    if(n == 0):
        return 0
    if(n == 1): 
        return 1
    return fib(n-1) + fib(n-2)

input = 4
print(fib(input)); # Output: 3