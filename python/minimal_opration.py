def minimalOperations(words):
    # Write your code here
    """ t(C) => O(nm) S(C) => O(n) """
    if len(words) == 0:
        
        return []
        
        
    substitutions = list()
    
    for word in words:
        
        i = 0
        count = 0
        while i+1 < len(word):
            
            if word[i] == word[i+1]:
                count += 1
                i += 2 #jump to third char
            else:
                i += 1 #jump to second char
         
        substitutions.append(count)
        
        
    return substitutions