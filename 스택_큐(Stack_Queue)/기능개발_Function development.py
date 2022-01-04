"""
progresses  작업 진도
speeds      작업 속도
"""
def solution(progresses, speeds):
    answer = []
    
    while (len(progresses) != 0) :
        progresses = [progress + speeds[idx] for idx, progress in enumerate(progresses)]
        
        if progresses[0] >= 100 :
            distCnt = 0
            for progress in progresses :
                if progress >= 100 : distCnt += 1
                else : break
            
            progresses = progresses[distCnt : len(progresses)]
            speeds = speeds[distCnt : len(speeds)]
            answer.append(distCnt)
    return answer