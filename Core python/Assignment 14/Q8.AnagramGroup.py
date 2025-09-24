#  Write a Python program to find all the anagrams and group them 
# together from a given list of strings.

def anagramGroup(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(words))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = anagramGroup(words)
print(res)

