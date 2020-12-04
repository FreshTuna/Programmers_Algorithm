def solution(prices):
    answer = [0] * len(prices)
    stack = []
    prices = list(zip(prices,list(range(0,len(prices)))))
    print(prices)
    for v,n in prices:
        if len(stack)==0:
            stack.append(prices[n])
        else:
            while len(stack)>0:
                temp=stack.pop()
                if temp[0] <= v:
                    stack.append(temp)
                    stack.append(prices[n])
                    break
                else : 
                    answer[temp[1]]=n-temp[1]
                    if len(stack)==0:
                        stack.append(prices[n])

    for i in range(len(stack)):
        answer[stack[i][1]]=n-stack[i][1]
                    
    return answer