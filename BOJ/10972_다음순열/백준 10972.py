import sys

n = int(sys.stdin.readline())

# 입력 값을 리스트로 받는다
case = list(map(int, sys.stdin.readline().split()))

# 변경할 수를 임시로 담을 공간
box = []

# 내림차순 여부를 체크하는 변수
# count가 수열의 크기와 같으면 수열 전체가 내림차순이므로 맨 마지막 수열이 된다.
count = 1

# 다음 수열 구하기 시작. 루프를 역순으로 돌린다.
# 첫 수가 아닌 끝 수에서부터 시작하는 것은 다이나믹 프로그래밍의 관점이다.
for i in range(n-1, 0, -1):
    # 현재 수가 이전의 수보다 클 경우 다음 수열이 존재한다는 뜻이다.
    # 다음에 올 수 있는 수열들 중 가장 앞 순번의 수열을 구한다.
    if case[i] > case[i-1] :
        box.append(case.pop()) # 일단 현재 수를 box에 담는다.
        temp = case.pop() # 이전의 수를 꺼내서 temp에 담는다.
        box.append(temp) # 이전의 수를 box에도 담는다.
        candidate = [] # 교체할 후보군을 담을 리스트 생성
        # box에 있는 수 중 temp보다 큰 수들은 모두 후보군이 된다.
        for num in box :
            if num > temp : candidate.append(num)
        # 후보군에 있는 수들 중 가장 작은 수로 교체한다.
        # 오름차순이 지켜질수록 앞 순번에 오기 때문이다.
        case.append(box.pop(box.index(min(candidate))))
        # 남은 수들을 정렬한다. 더 이상은 루프가 필요 없으므로 빠져나온다.
        box.sort()
        break
    # 내림차순이 유지되면 count를 늘린다.
    else : 
        box.append(case.pop())
        count+=1

# count가 수열의 크기와 같은 경우 맨 마지막 수열이다.
if count==n:print(-1)
# 아닐 경우 box에 있는 수열들을 차례대로 넣어 다음 수열을 완성시킨다.
else :
    for number in box :
        case.append(number)
    for answer in case :
        print(answer, end=' ')
        
