def solution(n):
    answer = n
    temp = (format(n,'b')).count('1')
    while True:
        answer +=1
        if (format(answer,'b')).count('1') == temp:
            break
            
    return answer