import sys

# 수열을 구해서 출력하는 함수
def sequence(index, n, m, seq) :
    # 수열의 길이가 m과 같으면 출력
    if len(seq)==m :
        for answer in seq :
            print(answer, end=' ')
        print()
    # 수열의 길이가 m과 다를 경우 함수 호출하여 다음 수열을 구한다
    else :
        # 반복문의 범위는 입력 받은 index부터 n까지다
        for i in range(index, n+1) :
            seq.append(i)
            sequence(i, n, m, seq)
            seq.pop()  # 수열의 길이를 유지하기 위해 함수 호출 후에는 pop을 한다

#main
n, m = map(int, sys.stdin.readline().split())
seq = [] # 수열을 저장할 리스
sequence(1, n, m, seq) # 재귀함수 호출

