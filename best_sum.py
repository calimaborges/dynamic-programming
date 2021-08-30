def best_sum(target, available_numbers, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if  target == 0:
        return []
    if target < 0:
        return None

    shortest_best_sum = None

    for number in available_numbers:
        remainder = target - number
        remainder_best_sum = best_sum(remainder, available_numbers, memo)

        if remainder_best_sum is not None:
            current_best_sum = [*remainder_best_sum, number]
            if shortest_best_sum is None or len(current_best_sum) < len(shortest_best_sum):
                shortest_best_sum = current_best_sum

    memo[target] = shortest_best_sum
    return memo[target]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))