def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    curW = 0
    curBridge = [] # Stack, FIFO
    while(len(truck_weights)+len(curBridge) != 0) :
        if len(curBridge) != 0 and curBridge[0]['loc'] == bridge_length :
            curW -= curBridge[0]['w']
            del curBridge[0]
            
        if len(truck_weights) != 0 and curW+truck_weights[0] <= weight :
            curTruck = truck_weights.pop(0)
            curBridge.append({'w' : curTruck, 'loc' : 0})
            curW += curTruck
            
        for truck in curBridge : truck['loc'] = truck['loc']+1
        answer += 1
        
    return answer