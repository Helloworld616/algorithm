# 실패

def solution(clothes):
    closet = dict()
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]] += 1
        else:
            closet[cloth[1]] = 1

    num_list = []
    for num in closet.values():
        num_list.append(num)

    answer = sum(num_list)
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            answer += num_list[i] * num_list[j]

    return answer


# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))