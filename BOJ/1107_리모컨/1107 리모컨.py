import sys

# 최소 버튼 조합 구하는 함수
def make_list(N, remote):
    # 결과를 담을 리스트 생성
    result = [[] for _ in range(len(N))]

    # N의 자릿수와 remote 안의 수들을 비교해 차이가 최소인 수들을 골라 result에 넣기
    for i in range(len(N)):
        min_num = abs(int(N[i]) - int(remote[0]))
        for j in range(1, len(remote)):
            if abs(int(N[i]) - int(remote[j])) <= min_num:
                min_num = abs(int(N[i]) - int(remote[j]))
        for j in range(len(remote)):
            if abs(int(N[i]) - int(remote[j])) == min_num:
                result[i].append(remote[j])

    # 결과값 반환
    return result

# 주어진 버튼에서 가능한 조합 결과들을 구하는 함수
def make_candidate(second, s_list, level, candidate):
    if level == len(s_list):
        candidate.append(second)
    else:
        for i in range(len(s_list[level])):
            second += s_list[level][i]
            make_candidate(second, s_list, level + 1, candidate)
            second = second[:len(second)-1] 


# main
# 입력 받기
N = sys.stdin.readline()
remote = [str(i) for i in range(10)]
b_num = int(sys.stdin.readline())

# 제외되는 버튼이 있을 경우 제외하기
if b_num > 0:
    broken = sys.stdin.readline().split()

    for button in broken:
        remote.pop(remote.index(button))

# N 오른쪽의 '\n' 없애기
N = N.rstrip()

# 첫번째 후보: 현재 수에서 채널까지의 거리 구하기
first = abs(int(N)-100)
min_count = first

# 버튼이 전부 고장나지 않았을 경우 두번째 후보 구하기
if b_num < 10:
    # 두번째 후보군: 최소로 버튼을 누를 수 있는 조합 구하기
    s_list = make_list(N, remote)

    # 두번째 후보군에서 나올 수 있는 모든 조합을 구해 리스트 candidate에 담기
    second = ''
    candidate = []
    make_candidate(second, s_list, 0, candidate)

    for i in range(len(candidate)):
        if int(candidate[i][0]) == 0:
            candidate[i] = candidate[i][1:] 


    # candidate 안의 값들과 first의 값을 비교해 N과의 차이가 가장 작은 값 구하기
    for number in candidate:
        if len(number) + abs(int(N) - int(number)) < min_count:
            min_count = len(number) + abs(int(N) - int(number))

# 세 번째 후보 구하기: 큰 값에서 감소할 때
for third in range(int(N), 1000001):
    if set(list(str(third))) & set(remote) == set(list(str(third))):
        third_num = len(str(third)) + third - int(N)
        if third_num < min_count:
            min_count = third_num

# 최소 입력 횟수 출력
print(min_count)
