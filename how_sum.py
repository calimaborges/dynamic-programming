def how_sum(target, available_numbers, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    
    for number in available_numbers:
        remainder = target - number
        remainder_sum = how_sum(remainder, available_numbers, memo)
        if remainder_sum is not None:
            memo[target] = [number, *remainder_sum]
            return memo[target]
        
    memo[target] = None
    return memo[target]

print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))