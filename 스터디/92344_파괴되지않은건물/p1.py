# 효율성 고려 X

def solution(board, skill):
    answer = 0
    for type, r1, c1, r2, c2, degree in skill:
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                if type == 1:       # 공격
                    board[x][y] -= degree
                elif type == 2:     # 회복
                    board[x][y] += degree

    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] > 0:
                answer += 1

    return answer



print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
# print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
