def count_write(target, word_bank, memo = None):
    if target == "":
        return 1
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    
    total = 0
    for word in word_bank:
        if target.startswith(word):
            total = total + count_write(target[len(word):], word_bank, memo)
        
    memo[target] = total
    return memo[target]

print(count_write("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_write("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_write("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_write("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    count_write(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]
    )
)