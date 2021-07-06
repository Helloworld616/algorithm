import sys

def lotto(case, result, idx):
    if len(result) == 6 :
        for number in result:
            print(number, end=' ')
        print()
    for i in range(idx, len(case)):
        result.append(case[i])
        lotto(case, result, i+1)
        result.pop()


while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers == [0] :
        break
    length = numbers[0]
    case = numbers[1:]
    
    for i in range(0, length-5):
        result = [ case[i] ]
        lotto(case, result, i+1)
        result.pop()
    print()

