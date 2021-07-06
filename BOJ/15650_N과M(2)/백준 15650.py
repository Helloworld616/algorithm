import sys

# 가지치기를 통해 수열을 생성하는 함수
def sequence(index, n, m, result) :
    # 만약 수열의 길이가 m과 같으면 출력하고 함수를 끝낸다
    if len(result)==m:
        for i in range(m):
            print(result[i], end=' ')
        print()
    # 아닐 경우 다음 원소를 추가하고 함수를 호출한다
    else :
        for i in range(index+1, n+1) :
            result.append(i)
            sequence(i, n, m, result)
            result.pop() # 중요!!! 수열의 길이를 유지하기 위해 다음 인덱스로 가기 전 pop하기


#main
n, m = map(int, sys.stdin.readline().split())

# 첫 번째 숫자를 집어넣은 뒤, 그 숫자보다 큰 수열을 차례대로 찾아가보자 
for i in range(1, n+1) :
    result = []
    result.append(i) # 첫 번째 숫자를 집어넣는다
    sequence(i, n, m, result) # 재귀함수 호출, 가지치기 시작
