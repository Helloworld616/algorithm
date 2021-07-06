import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    iron_bar = input()

    cnt = 0 # 막대 수
    ans = 0 # 정답

    for i in range(len(iron_bar)):
        # 열린 괄호라면 막대 추가
        if iron_bar[i] == '(':
            cnt += 1
        else:
            # 닫힌 괄호라면 막대 감소
            # 레이저라면 당연히 잘못 세었으니까 빼는게 맞다.
            # 아니라면 어차피 철봉 끝이니 빼는게 맞다.
            cnt -= 1

            # 레이저라면
            if iron_bar[i-1] == '(':
                # 레이저로 인해서 잘린 막대들이 생겼으므로
                ans += cnt
            else:
                # 막대 끝이라는 뜻
                ans += 1