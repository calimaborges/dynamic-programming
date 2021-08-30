def all_write(target, word_bank, memo = None):
    if target == "":
        return [[]]
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    
    ways_to_write = []
    for word in word_bank:
        if target.startswith(word):
            suffix_writes = all_write(target[len(word):], word_bank, memo)
            ways_to_write = ways_to_write + list(map(lambda w: [word, *w], suffix_writes))

    memo[target] = ways_to_write
    return memo[target]

print(all_write("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_write("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_write("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_write("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    all_write(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]
    )
)