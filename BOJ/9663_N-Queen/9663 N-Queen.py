import sys

def NQueen(queen, q_num, cnt, N):
    if q_num == N+1:
        cnt[0] += 1
    else:
        for i in range(1, N + 1):
            move = True
            for j in range(1, q_num):
                if i == queen[j] or abs(i - queen[j]) == abs(q_num - j):
                    move = False
                    break
            if move:
                queen[q_num] = i
                NQueen(queen, q_num + 1, cnt, N)
                
                    
# main
N = int(sys.stdin.readline())
queen = [0] * (N + 1)
cnt = [0]
q_num = 1

for i in range(1, N + 1):
    queen[q_num] = i    
    NQueen(queen, q_num + 1, cnt, N)

print(cnt[0])
