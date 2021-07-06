def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        bubble_sort(box)
        box[0] += 1
        box[-1] -= 1

    bubble_sort(box)

    print("#{} {}".format(tc, box[-1]-box[0]))