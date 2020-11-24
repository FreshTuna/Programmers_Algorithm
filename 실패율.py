def solution(N, stages):
    answer = []
    temp = []
    len_stage = len(stages)
    
    for i in range(1,N+1):
        index=0
        for j in range(len(stages)):
            if stages[j] == i: 
                index +=1
        temp.append(index/len_stage)
        len_stage = len_stage-index
        if len_stage == 0:
            temp +=[0]*(N-i)
            break
    
    for i in range(len(temp)):
        answer.append(temp.index(max(temp))+1)
        temp[temp.index(max(temp))]=-1
        
    return answer