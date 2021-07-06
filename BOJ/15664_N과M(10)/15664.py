import sys

def sequence(numbers, result, idx, n):
    if len(result) == n :
        for number in result:
            print(number, end = ' ')
        print()
    if len(set(numbers[idx:])) < len(numbers[idx:]) :
        number_info = {}
        for number in numbers[idx:]:
            if number not in number_info:
                number_info[number] = numbers.index(number, idx)
        for number, location in number_info.items():
            result.append(number)
            sequence(numbers, result, location+1, n)
            result.pop()
    else :
        for i in range(idx, len(numbers)):
            result.append(numbers[i])
            sequence(numbers, result, i+1, n)
            result.pop()
        
    
            
# main
m, n = map(int, sys.stdin.readline().split())

# 입력 받은 수들을 리스트로 변환
numbers = list(map(int, sys.stdin.readline().split()))

# 리스트 정렬
numbers.sort()
result = []
sequence(numbers, result, 0, n)
