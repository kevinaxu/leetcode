



# add memoization
def canSum(target, arr, memo={}) -> bool:
    # Base Case: Check Memo
    if target in memo:
        print("in memo!")
        return memo[target]

    # Base Cases
    if target == 0: return True
    if target < 0: return False

    for n in arr:
        diff = target - n
        print(f"canSum({diff}, {arr})")

        status = canSum(diff, arr, memo)
        if status:
            return True
        else:
            memo[diff] = status
    return False


print(canSum(81, [5, 3, 4, 7]))


'''
# TODO: can I do this but store the paths? 
# TODO: how can we optimize this further? gridTraveler(1, 3) ~ gridTraveler(3, 1)
def gridTraveler(m, n, memo={}) -> int:
    coord = (m, n)
    print(f"traversing ({m}, {n})")
    if coord in memo:
        print("in memo!")
        return memo[coord]

    # Base Cases
    if m == 0 or n == 0:  return 0
    if m == 1 and n == 1: return 1 

    memo[(m, n)] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[coord]


# print(gridTravelerWithPath(1, 1))   # 1
print(gridTravelerWithPath(18, 18))   # 2333606220
# print(gridTravelerWithPath(3, 2))   # 3
# print(gridTravelerWithPath(3, 3))   # 6
'''


'''
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
'''

