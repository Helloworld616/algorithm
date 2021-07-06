import sys


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

table = []
for i in range(n):
    case = [numbers[j] for j in range(n)]
    table.append(case)
#print(table)

for i in range(n):
    # 첫 번째 수를 행의 가장 큰 수 large에 넣는다.
    large = numbers[i]
    large_sum = numbers[i]
    # 다음 수부터 루프를 돌린다.
    for j in range(i+1, n):
        if numbers[j] > large:
            table[i][j] = max(large_sum + numbers[j], table[i][j-1] + numbers[j]) 
            large = numbers[j]
            large_sum = table[i][j]
        else :
            if numbers[j] > numbers[i]:
                if numbers[j] > numbers[j-1]:
                    table[i][j] = table[i][j-1] + numbers[j]
                else : 
                    table[i][j] = numbers[i] + numbers[j]
            if table[i][j] > large_sum:
                large_sum = table[i][j]
#print(table)
maximum = max(table[0])



for i in range(1, n) :
    if maximum < max(table[i]):
        maximum = max(table[i])

print(maximum)
    
