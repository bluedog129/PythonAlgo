strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']

def matchingStrings(strings, queries):
    results = list(0 for i in range(len(queries)))
    
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                count += 1
                
        results[i] = count
            
    return results

print(matchingStrings(strings, queries))