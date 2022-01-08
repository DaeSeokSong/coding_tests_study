"""
priorities  중요도 (숫자 ↑ == 중요도 ↑) 및 대기 순서 (0 1 2 3 ~)
location    요청한 문서의 대기 순번
"""
def solution(priorities, location):
    answer = 0
    outDoc = ''
    
    while(len(priorities) > 0) :
        prtFlag = True
        curPrior = priorities.pop(0)
        for idx, prior in enumerate(priorities) :
            if prior > curPrior :
                priorities.append(curPrior)
                prtFlag = False
                break
                
        if prtFlag :
            answer += 1
            if location == 0 : break
                
        if location <= 0 : location = len(priorities)-1
        else : location -= 1
    
    return answer