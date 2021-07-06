import sys
sys.stdin = open('input.txt')

T = int(input())
t = 1

for _ in range(T):
    # 입력 숫자를 리스트로 바꾼다.
    numbers = list(map(int, input().split()))
    total = 0
    average = 0
    # 리스트의 총 합을 구한다.
    for number in numbers:
        total += number
    # 총 합을 리스트 원소 개수로 나눈다.
    average = round(total/len(numbers))
    print('#{} {}'.format(t, average))
    t += 1


