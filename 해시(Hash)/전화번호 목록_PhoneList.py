def solution(phone_book):
    answer = True
    
    for idx, phone in enumerate(phone_book) :
        print(len(phone))
        if len(phone) == 20 : continue
        else : 
            candi_phone = [p[0 : len(phone)] for p in (phone_book[0 : idx] + phone_book[idx+1 : len(phone_book)]) if phone in p]
            if phone in candi_phone : 
                answer = False
                break   
    return answer