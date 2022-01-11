def solution(participant, completion):
    answer = ''
    
    dic_participant = {}
    for prtct in participant :
        if prtct not in dic_participant.keys() : dic_participant[prtct] = 0
        else : dic_participant[prtct] += 1
    
    for com_prtct in completion : 
        dic_participant[com_prtct] -= 1
        if dic_participant[com_prtct] < 0 : del dic_participant[com_prtct]
            
    answer = list(dic_participant.keys())[0]
    return answer