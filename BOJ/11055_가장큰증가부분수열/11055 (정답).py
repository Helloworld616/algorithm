import sys


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
compare = [0 for i in range(n)]
maximum = 0

for i in range(0, n):
    compare[i] = numbers[i]
    for j in range(0, i):
        if numbers[j] < numbers[i] :
            if compare[i] < compare[j] + numbers[i]:
                compare[i] = compare[j] + numbers[i]
    if maximum < compare[i]:
        maximum = compare[i]

print(maximum)
        
