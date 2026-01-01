class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # 열린 괄호들을 넣을 스택
        is_vp = True # 유효한 괄호들인지 결정할 최종 결과 변수
        pairs = { # 각 짝을 이루는 괄호들 dictionary 형태로 선언
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for ch in s:
            if ch in pairs: # 만약 열린 괄호가 pairs 딕셔너리에 있으면 스택에 넣는다.  
                stack.append(ch)

            else:
                if len(stack) == 0: # 만약 바로 닫힌 괄호가 나오면 False를 반환한다. 
                    is_vp = False
                    break

                open_bracket = stack.pop() # 스택에서 열린 괄호를 꺼낸다. 

                if pairs[open_bracket] != ch: # 스택에서 꺼낸 열린 괄호랑 닫힌 괄호랑 비교했을 때 짝이 안맞으면 False 반환 
                    is_vp = False
                    break

        if len(stack) != 0: # 최종적으로 스택에 무언가 남아있으면 (예를들어 "(((" 처럼 열린 괄호만 있는경우) False 반환 
            is_vp = False
            return is_vp
        
        else: # 모두 통과했으면 True 반환 
            return is_vp
        