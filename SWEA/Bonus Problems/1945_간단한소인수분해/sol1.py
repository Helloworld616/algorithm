import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    number = int(input())
    prime = [2, 3, 5, 7, 11]
    answers = []
    for num in prime:
        answer = 0
        while number % num == 0:
            number //= num
            answer += 1
            if number == 1:
                break
        answers.append(answer)
    print('#{}'.format(i), end = ' ')
    for idx in range(len(answers)):
        if idx == len(answers)-1:
            print(answers[idx])
        else:
            print(answers[idx], end = ' ')