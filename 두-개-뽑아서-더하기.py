def solution(numbers):
    answer = set()
    len_num = len(numbers)
    for i in range(len_num):
        for j in range(len_num):
            if i==j:
                continue
            answer.add(numbers[i]+numbers[j])
            
    return sorted(list(answer))