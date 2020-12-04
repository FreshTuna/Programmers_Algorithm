import math

def solution(progresses, speeds):
    answer = []
    while len(progresses)>0:
        Need = math.ceil((100 - progresses[0])/speeds[0])
        index = 0
        progresses = [progresses[i] + (speeds[i] * Need) for i in range(len(progresses))]

        for i in range(len(progresses)):
            if progresses[i]>99:
                index+=1
            else:
                break
        
        for i in range(index):
            progresses.pop(0)
            speeds.pop(0)
        
        answer.append(index)
        
    return answer