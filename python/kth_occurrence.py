def kthOccurrence(X, arr, query_values):
    # Write your code here
    """ T(C) => O(n), S(C) => (n)"""
    occurrences = list()
    
    num_multiple = dict()
    # get all 1-based index of X from arr
    occurrence_indices = [index+1 for index, num in enumerate(arr) if num == X]
    
    #get multiples of all numbers from arr
    for num in arr:
        num_multiple[num] = num_multiple.get(num, 0) + 1
        
         
    for q in query_values:
        
        multiple = num_multiple.get(X)
        
        if multiple >= q:
            #get and append qth based index for X if exists
            occurrences.append(occurrence_indices[q-1])
            
        else:
            occurrences.append(-1)
            
    return occurrences