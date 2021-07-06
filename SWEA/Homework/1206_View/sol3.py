# 정원이 님 코드

tc = 10

for t in range(tc):

    n = input()
    tmp = input()
    building = tmp.split()
    ans = 0

    for i in range(2, n-2):
        nearby = max(int(building[i-2]), int(building[i-1]), int(building[i+1]), int(building[i+2]))
        if int(building[i]) > int(nearby):
            ans += int(building[i]) - int(nearby)

    print('#{} {}'.format(t+1, ans))