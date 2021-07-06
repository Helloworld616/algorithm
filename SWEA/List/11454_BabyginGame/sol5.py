def perm(idx, length):
    if idx == length:
        point = 0
        # triplet
        if arr[0] == arr[1] == arr[2]:
            point += 1
        if arr[3] == arr[4] == arr[5]:
            point += 1
        # run
        if arr[0] + 1 == arr[1] and arr[1] * 1 == arr[2]:
            point += 1
        if arr[3] + 1 == arr[4] and arr[4] * 1 == arr[5]:
            point += 1

        if point == 2:
            print('BABYGIN', arr)
    else:
        for changer in range(idx, length):  # idx ~ 끝까지
            arr[idx], arr[changer] = arr[changer], arr[idx]  # 현재 숫자 유지부터, 오른쪽 끝까지 교환
            perm(idx + 1, length)  # 다음번 자리 결정하러 이동(n개 결정)
            arr[idx], arr[changer] = arr[changer], arr[idx]  # 복구
            

arr = [1, 1, 1, 2, 2, 2]
cnt = 0
perm(0, 6)

print(cnt)
