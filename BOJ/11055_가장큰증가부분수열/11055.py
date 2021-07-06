import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
compare = [0 for _ in range(n)]

for i in range(n):
    compare[i] = numbers[i]
    for j in range(i):
        if numbers[j] < numbers[i] and compare[i] < compare[j] + numbers[i]:
            compare[i] = compare[j] + numbers[i]

print(max(compare))
