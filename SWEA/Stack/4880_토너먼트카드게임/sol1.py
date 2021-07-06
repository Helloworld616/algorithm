import sys
sys.stdin = open('sample_input.txt')


def winner(A, B):
    if A[0] == B[0]:
        if A[1] < B[1]:
            return A
        else:
            return B
    else:
        if A[0] == 1:
            if B[0] == 2:
                return B
            else:
                return A
        if A[0] == 2:
            if B[0] == 3:
                return B
            else:
                return A
        if A[0] == 3:
            if B[0] == 1:
                return B
            else:
                return A


def fight(students, start, end, answer):
    if end - start == 1:
        answer.append(winner(students[start-1], students[end-1]))
    elif end - start == 0:
        answer.append(students[start-1])
    else:
        middle = (start + end) // 2
        fight(students, start, middle, answer)
        fight(students, middle+1, end, answer)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    students = []
    for i in range(1, N+1):
        students.append((numbers[i - 1], i))

    answer = []
    start = 1
    end = N
    while len(students) > 1:
        fight(students, start, end, answer)
        students = answer[:]
        answer = []
        start = 1
        end = len(students)

    print('#{} {}'.format(tc, students[0][1]))

