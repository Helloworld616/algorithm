import sys
sys.stdin = open("input.txt")


def max_palindrome(words, num):
    for i in range(100):
        for j in range(100 - num + 1):
            for k in range(num//2):
                if words[i][j+k] != words[i][j+num-k-1]:
                    break
                if k + 1 == num//2:
                    return num

            for k in range(num//2):
                if words[j+k][i] != words[j+num-k-1][i]:
                    break
                if k + 1 == num//2:
                    return num

    return 0


for tc in range(1, 11):
    T = input()
    words = []
    for i in range(100):
        word = input()
        words.append(word)

    for i in range(100, 0, -1):
        answer = max_palindrome(words, i)

        if answer != 0:
            break

    print('#{} {}'.format(tc, answer))