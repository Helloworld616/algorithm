import sys

def sequence(numbers, number_list, idx, n) :
    # 결과 리스트의 길이가 n과 같으면 출력
    if len(number_list) == n :
        for number in number_list :
            print(number, end = ' ')
        print()
    # 결과 리스트의 길이가 n과 같지 않을 경우 원소 추가 후 함수 호출
    else :
        for i in range(idx, len(numbers)) :
            number_list.append(numbers[i])
            sequence(numbers, number_list, i+1, n)
            number_list.pop()


# main
m, n = map(int, sys.stdin.readline().split())

# 입력 받은 수들을 리스트로 변환
numbers = list(map(int, sys.stdin.readline().split()))

# 리스트 정렬
numbers.sort()

# 결과 리스트 생성 후 함수에 넣기
for i in range(len(numbers)):
    number_list = []
    number_list.append(numbers[i])
    # 이미 추가된 원소는 이후 추가되는 원소에서 제외되어야 함
    # 함수 호출 시 현재 index보다 1만큼 더 큰 index 입력
    sequence(numbers, number_list, i+1, n)
