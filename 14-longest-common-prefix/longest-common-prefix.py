class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        mn_word = "" # 최소 길이를 가진 문자
        mn_length = 300 # 최소 문자 길이 
        
        for word in strs: # 최소 길이를 가진 문자를 찾아내는 로직 
            if len(word) < mn_length:
                mn_length = len(word)
                mn_word = word 

        rst = "" # 반환할 결과

        for i in range(0,len(mn_word),1):
           ch = mn_word[i] # (최소 길이를 가진)기준 문자의 한글자

           for word in strs:
               if ch != word[i]: # 만약 공통 글자가 다르면 거기서까지만 stop하고 rst를 return 한다.
                   return rst

           rst += ch # 모두 통과하면(공통 단어는) rst에 붙여준다. 
            
               
        return rst 