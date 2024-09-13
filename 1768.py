# Merge Strings



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        ans =[]
        n = len(word1)
        m =len(word2)
        while i < n and j < m:
            ans.append(word1[i])
            ans.append(word2[j])

            i +=1
            j +=1

        ans.append(word1[i:])
        ans.append(word2[j:])
        return "".join(ans)

        
        
        
        
        return ans

        
