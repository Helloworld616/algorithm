import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
need = []

for i in range(len(A)):
    A[i] -= B

for i in range(len(A)):
    if A[i] <= 0:
        need.append(0)
    else:
        supply = A[i] // C
        if A[i] % C > 0 :
            supply += 1
        need.append(supply)

total = N
for number in need:
    total += number

print(total)

    
