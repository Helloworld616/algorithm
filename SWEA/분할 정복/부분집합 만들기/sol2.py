# 비트 마스크

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 주어진 리스트
N = len(arr)  # 리스트의 길이 저장

# 비트 마스크를 활용한 반복문 실행
for i in range(1 << N):
    # 부분 집합을 담을 리스트 powerset 생성
    powerset = []
    for j in range(N):
        # i의 j번째 비트가 1인 경우
        if i & 1 << j:
            # 리스트에 원소 추가
            powerset.append(arr[j])
    # 완성된 부분집합의 총합이 10일 경우 출력
    if sum(powerset) == 10:
        print(powerset)
