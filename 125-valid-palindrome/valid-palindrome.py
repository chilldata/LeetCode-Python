class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = s.lower() # 모두 소문자로 바꿔준다. 
        st2 = "" # 모두 대문자 및 다른 문자 아스키 코드를 다 제외하여 포함한 문자열 

        for ch in st: # 소문자와 숫자 이외의 모든 아스키 코드 문자들은 제외한 후 st2에 넣어준다.
            o = ord(ch)
            if (ord("a") <= o <= ord("z")) or (ord("0") <= o <= ord("9")):
                st2 += ch


        for i in range(0,len(st2),1):
            left = i # 가장 왼쪽 index
            right = len(st2) - (i+1) # 가장 오른쪽 끝 index

            if st2[left] != st2[right]: # 만약 양 끝이 서로 다르면 바로 False를 반환 
                return False


        return True # 모두 통과하면 True 반환 