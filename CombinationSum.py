#Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

#The same repeated number may be chosen from candidates unlimited number of times.

def combinationSum(candidates, target):
    results= []
    combination =[]
    startIndex = 0
    dfs(candidates,target,combination, startIndex,results)
    return results

def dfs(candidates, target, combination, startIndex, results):
    if target < 0:
      return 
    if target == 0:
            results.append(combination)
            return
    for i in range(startIndex, len(candidates)):
            combinationCopy = combination.copy()
            combinationCopy.append(candidates[i])
            dfs(candidates, target-candidates[i], combinationCopy, i, results)
    return 
print(combinationSum([2,4,1],4))

        



