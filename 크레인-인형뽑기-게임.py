def solution(board, moves):
    answer = 0
    basket = []

    
    for i in range(len(moves)):
        index = 0
        while index < len(board):
            NOW = board[index][moves[i]-1]
            if NOW!=0:
                basket.append(NOW)
                if len(basket)>1 and basket[-1:] == basket[-2:-1]:
                    answer +=1
                    del basket[-2:]
                board[index][moves[i]-1]=0
                break
            else :
                index = index + 1
    return answer*2