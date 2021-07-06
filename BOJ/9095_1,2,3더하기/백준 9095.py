import sys

# 새로운 식을 도출하는 재귀함수
def change(start, result, index_1, index_2) :
    # 식이 두 개 이상의 숫자로 이루어져 있고, 두 수의 합이 4 미만일 때 함수 실행
    if len(start) > 1 and (start[index_1]+start[index_2])<4 :
        
        next = [] # 새로운 식을 담을 리스트 생성
        
        # 리스트에 새로운 식을 담는다 
        for i in range(len(start)) :
            if i != index_2 :
                if i==index_1:
                    next.append(start[index_1]+start[index_2])
                else : next.append(start[i])
                
        # 새로운 식이 완성되면, 결과값 안에 있는지 없는지 확인한다. 없으면 추가.
        count = 0
        for i in range(len(result)):
            if result[i] == next : count+=1
        if count==0 : result.append(next)

        # 현재 식으로부터 다음 식을  도출한다.
        for i in range(len(next)-1) :
            change(next, result, i, i+1)
        

n = int(sys.stdin.readline()) # 테스트 케이스 갯수 입력

for i in range(n) : # 테스트 케이스 갯수 만큼 루프
    m = int(sys.stdin.readline()) # 테스트 케이스 입력
    start = [] # 첫 식을 담을 리스트
    result = [] # 모든 결과값을 담을 리스트

    # 첫 번째 식은 모두 1로 이루어져 있다.
    for i in range(m) :
        start.append(1)

    # 첫 번째 식을 결과값에 추가
    result.append(start)

    # 첫 번째 식으로부터 다음 식을 도출한다.
    for i in range(m-1) :
        change(start, result, i, i+1) # 재귀함수 호출

    print(len(result))

