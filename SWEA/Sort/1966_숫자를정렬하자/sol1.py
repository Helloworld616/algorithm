import sys
sys.stdin = open('input.txt')


def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    # pivot을 기준으로 pivot보다 작은 숫자들은 left에, 큰 숫자들은 right에 모은다.
    left = []
    right = []
    pivot = nums[0]

    for idx in range(1, len(nums)):
        if nums[idx] < pivot:
            left.append(nums[idx])
        else:
            right.append(nums[idx])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return [*sorted_left, pivot, *sorted_right]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, quick_sort(numbers)))