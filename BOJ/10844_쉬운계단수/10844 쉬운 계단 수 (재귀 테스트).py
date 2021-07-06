def easy_stair(stair, cnt, N):
    if len(stair) == N:
        #if stair[0]== 8:
            #print(stair)
        cnt[0] += 1
    else:
        for i in range(10):
            if abs(stair[len(stair)-1] - i) == 1:
                stair.append(i)
                easy_stair(stair, cnt, N)
                stair.pop()


N = int(input())
cnt = [0]

for i in range(1, 10):
    easy_stair([i], cnt, N)

print(cnt[0])
