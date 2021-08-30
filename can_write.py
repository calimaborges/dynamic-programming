def can_write(target, word_bank, memo = None):
    if target == "":
        return True
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    
    for word in word_bank:
        if target.startswith(word):
            if can_write(target[len(word):], word_bank, memo):
                memo[target] = True
                return memo[target]

    memo[target] = False
    return memo[target]

print(can_write("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_write("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_write("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_write(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]
    )
)