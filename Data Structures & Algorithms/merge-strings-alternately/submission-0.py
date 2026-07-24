class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        string=[]
        while i< len(word1) and j<len(word2):
            string.append(word1[i])
            string.append(word2[j])
            i+=1
            j+=1
        string.extend(word1[i:])  
        string.extend(word2[j:])
        return "".join(string)