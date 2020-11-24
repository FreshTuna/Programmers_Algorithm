from math import pow

def solution(n):
    answer = 0
    temp = []
    while n!=0:
        if n < 3 : 
            temp.append(n)
            n = 0
        elif n % 3 == 0 :
            temp.append(0)
            n = n/3
        else:
            temp.append(n%3)
            n = int(n/3)
            
    for i in range(len(temp)):
        answer += pow(3,len(temp)-i-1) * temp[i]
        
    return answer