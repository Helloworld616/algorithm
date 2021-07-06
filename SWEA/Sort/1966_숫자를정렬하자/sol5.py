import sys
sys.stdin = open('input.txt')


def merge_sort(numbers):
    N = len(numbers)
    if N < 2:
        return numbers

    mid_idx = N // 2
    left = numbers[:mid_idx]
    right = numbers[mid_idx:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    merged = []
    l = r = 0
    while l < len(sorted_left) and r < len(sorted_right):
        if sorted_left[l] < sorted_right[r]:
            merged.append(sorted_left[l])
            l += 1
        else:
            merged.append(sorted_right[r])
            r += 1

    merged += sorted_left[l:]
    merged += sorted_right[r:]
    return merged


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sorted_numbers = merge_sort(numbers)
    print(f'#{tc} {sorted_numbers}')
