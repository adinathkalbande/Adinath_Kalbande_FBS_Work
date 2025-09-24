def longestCommonPrefix(words):
    if not words:
        return ""
    
    prefix = ""
    first = words[0]      
    for i in range(len(first)):
        chars = set() 
        for word in words:
            if i < len(word):     
                chars.add(word[i])
            else:
                return prefix     
        
        if len(chars) == 1:      
            prefix += chars.pop()
        else:
            break
    
    return prefix
words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longestCommonPrefix(words))
