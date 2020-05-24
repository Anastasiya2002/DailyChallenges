#Given a string containing digits from 2-9 inclusive, 
#return all possible letter combinations that the number could represent.
def letterCombinations(digits):
        result=[]
        letters = {'2':"abc", '3':"def",'4':"ghi", '5':"jkl", 
       '6':"mno", '7':"pqrs", '8':'tuv', '9':"wxyz"}        
        def dfs(path, digits):
          if len(digits) <= 0:
            return result.append(path)
          for i in letters[digits[0]]:
              dfs(path + i, digits[1:])
        if digits:
              dfs("",digits)
        return result
print(letterCombinations('23'))

        
    
        