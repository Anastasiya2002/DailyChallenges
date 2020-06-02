def combinationSum2(candidates, target):
    candidates.sort()
    results = []
    combination = []
    startIndex = 0
    dfs(candidates,target,combination,startIndex,results)
    return results

def dfs(candidates, target, combination, startIndex, results):
    if target < 0:
      return 
    if target == 0:
            if combination not in results:
                results.append(combination)
            return
    for i in range(startIndex, len(candidates)):
            combinationCopy = combination.copy()
            combinationCopy.append(candidates[i])
            dfs(candidates, target-candidates[i], combinationCopy, i+1, results)
    return 

print(combinationSum2([2,5,2,1,2],5))