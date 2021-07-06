import sys

def sequence(numbers, result):
    # 초기 리스트가 다 비는 순간 결과 리스트 출력
    if len(numbers)==0:
        for num in result :
            print(num, end=' ')
        print()
    # 초기 리스트로부터 가지치기 시작
    for number in numbers:

        # 초기 리스트에서 원소를 하나씩 추출해서 결과 리스트를 만든다.  
        result.append(number) # 추출한 원소를 결과 리스트에 담기
        idx = numbers.index(number) # 초기 리스트에서 추출한 원소의 index를 기억해둔다.
        numbers.pop(idx) # 추출한 원소를 결과 리스트에서 제거한다.
        
        # 변경된 초기 리스트와 결과 리스트로 다시 가지치기 시작 
        sequence(numbers, result)

        # 초기 리스트와 결과 리스트를 다시 원래대로 돌려놓는다.
        numbers.insert(idx, number) # 제거했던 원소를 원래 index에 다시 추가
        result.pop() # 추가했던 원소를 다시 제거

# main    
n = int(sys.stdin.readline())
numbers = []

# 초기 리스트 생성
for i in range(1, n+1):
    numbers.append(i)

# 결과 값을 담을 빈 리스트 생성 
result = []

# 순열 생성 함수 호출
sequence(numbers, result)

