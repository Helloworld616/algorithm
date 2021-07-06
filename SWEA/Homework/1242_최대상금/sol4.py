import sys
sys.stdin = open('input.txt')


def backtrack(k):
    global ans, N
    val = int(''.join(cards))
    if val in visited[k]:
        return
    visited[k].add(val)

    # 최종 교환 완료라면, 최댓값 갱신
    if k == cnt:
        ans = max(ans, val)
    else:
        for i in range(N-1):
            for j in range(i, N):
                cards[i], cards[j] = cards[j], cards[i]
                backtrack(k+1)
                cards[i], cards[j] = cards[j], cards[i]


T = int(input())

for tc in range(1, T+1):
    input_data = list(input().split())
    cards, cnt = list(input_data[0]), int(input_data[1])

    N = len(cards)
    visited = [set() for _ in range(11)]
    ans = 0
    backtrack(0)
