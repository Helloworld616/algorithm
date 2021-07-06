nums = [1, 2, 3]


def perm(idx, length):
    if idx == length:
        print(*nums)
    else:
        for changer in range(idx, length):
            nums[idx], nums[changer] = nums[changer], nums[idx]
            perm(idx+1, length)
            nums[idx], nums[changer] = nums[changer], nums[idx]


perm(0, len(nums))
