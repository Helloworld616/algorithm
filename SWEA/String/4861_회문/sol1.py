import sys
sys.stdin = open('sample_input.txt')


def palindrome(strings, N, M):
    for i in range(N):
        for j in range(N - M + 1):
            cnt = 0
            palindrome = ''
            for k in range(M // 2):
                if strings[i][j + k] == strings[i][j + M - k - 1]:
                    palindrome += strings[i][j + k]
                    cnt += 1
            if cnt == M // 2:
                answer = palindrome
                if M % 2:
                    answer += strings[i][j + k + 1]
                for idx in range(len(palindrome) - 1, -1, -1):
                    answer += palindrome[idx]
                return answer

    for i in range(N):
        for j in range(N - M + 1):
            cnt = 0
            palindrome = ''
            for k in range(M // 2):
                if strings[j + k][i] == strings[j + M - k - 1][i]:
                    palindrome += strings[j + k][i]
                    cnt += 1
            if cnt == M // 2:
                answer = palindrome
                if M % 2:
                    answer += strings[j + k + 1][i]
                for idx in range(len(palindrome) - 1, -1, -1):
                    answer += palindrome[idx]
                return answer


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    strings = []
    for i in range(N):
        string = input()
        strings.append(string)

    answer = palindrome(strings, N, M)
    print('#{} {}'.format(tc, answer))

