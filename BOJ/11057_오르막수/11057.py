import sys

n = int(sys.stdin.readline())

table = [[ 1 for i in range(0, 10)]]

for i in range(1, n):
    info = [ 1 ]
    for j in range(8, -1, -1):
        cnt = table[i - 1][j] + info[0]
        info.insert(0, cnt)
    table.append(info)

print(sum(table[-1]) % 10007)
    
