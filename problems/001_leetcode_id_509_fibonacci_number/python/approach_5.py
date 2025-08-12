
#  Method 5: Binet's Formula (Closed-form expression)

def fib(n):
        sqrt5 = 5 ** 0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)

input = 4
print(fib(input)); # Output: 3