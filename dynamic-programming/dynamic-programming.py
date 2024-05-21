

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 0:
        return 1
    memo[n] = fib(n - 1, memo) + fib (n - 2, memo)
    print(f"setting memo: {n} {memo[n]}")
    return memo[n]

print(f"result: {fib(10)}")


# idx 0 1 2 3 4 5
# val 1 1 2 3 5 8 

