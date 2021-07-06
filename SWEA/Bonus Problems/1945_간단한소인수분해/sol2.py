T = int(input())

for tc in range(1, T+1):
    N = int(input())

    prime = [2, 3, 5, 7, 11]

    cnt = [0] * 5 # 정답을 위한 개수 세기

    # 주어진 소수의 수만큼 반복
    for i in range(len(prime)):
        while N % prime[1] == 0:
            cnt[i] += 1
            N //= prime[i]

    print('#{} {}'.format(tc, ' '.join(map(str, cnt))))