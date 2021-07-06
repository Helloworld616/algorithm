import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# A.sort()
# B.sorted(reverse=True)

for i in range(n-1):
    for j in range(i, n):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
        if B[i] < B[j]:
            B[i], B[j] = B[j], B[i]

answer = 0
for i in range(n):
    answer += A[i] * B[i]

print(answer)
