import sys
    
N = int(sys.stdin.readline())
fibonacci = [0, 1]

for i in range(2, N+1):
    fibonacci += [fibonacci[i - 1] + fibonacci[i - 2]]

print(fibonacci[N])
