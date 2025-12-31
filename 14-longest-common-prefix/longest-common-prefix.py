class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        mn_word = ""
        mn_length = 300
        
        for word in strs:
            if len(word) < mn_length:
                mn_length = len(word)
                mn_word = word 

        rst = "" 

        for i in range(0,len(mn_word),1):
           ch = mn_word[i] 

           for word in strs:
               if word[i] != ch:
                   return rst

           rst += ch
            
               
        return rst 