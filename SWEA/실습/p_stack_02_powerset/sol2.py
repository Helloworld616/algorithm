data = list(range(1, 11))
is_selected = [None] * len(data)
results = []


def power_set(idx):
    if idx == len(data):
        return # 함수 끝내기
    else:
        is_selected[idx] = True
        power_set(idx + 1)
        is_selected[idx] = False
        power_set(idx + 1)


def power_set2(idx):
    # is_selected를 다 채우지 못했다면
    if idx < len(data):
        is_selected[idx] = True
        power_set(idx + 1)
        is_selected[idx] = False
        power_set(idx + 1)
    # 다 채웠다면 (idx == len(data))
    else:
        total = 0
        for i in range(len(data)):
            if is_selected[i]:
                total += data[i]
        
        if total == 10:
            results.append(is_selected[:])
        
        return None # 함수 끝

power_set(0)

for result in results:
    print(result)
