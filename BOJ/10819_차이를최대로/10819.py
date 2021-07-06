import sys

def total(table, num, visit, idx):
    visit[idx] = 1
    maximum = 0
    
    for i in range(len(table[idx])):
        if visit[i] == 0 and table[idx][i] > maximum :
            maximum = table[idx][i]
            location = i
            
    if visit.count(1) == len(table[idx]):
        return num
            
    return num + total(table, maximum, visit, location)


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

table = []

for number1 in numbers:
    case = []
    for number2 in numbers:
        case.append(abs(number1 - number2))
    table.append(case)

candidate = []
for i in range(0, n):
    for j in range(0, n):
        if i != j :
            visit = [0 for i in range(n)]
            visit[i] = 1
            candidate.append(total(table, table[i][j], visit, i))
            print(visit)
print(candidate)

maximum = candidate[0]
for number in candidate:
    if number > maximum:
        maximum = number

print(maximum)
