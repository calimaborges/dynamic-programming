def can_sum(target, available_numbers, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    
    for number in available_numbers:
        remainder = target - number
        if (can_sum(remainder, available_numbers, memo)):
            memo[target] = True
            return True
        
    memo[target] = False
    return False

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))