#Given an array of strings, group anagrams together.
import collections
from collections import Counter
def groupAnagrams(strs):
    results = []
    found = False
    for i in strs:
        found = False
        for result in results:
            if Counter(result[0]) - Counter(i) == Counter():
                result.append(i)
                found = True
        if not found:
            results.append([i])
        
    return results

print(groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))

