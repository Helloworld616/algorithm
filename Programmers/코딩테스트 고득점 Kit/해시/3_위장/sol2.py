from itertools import combinations


def solution(clothes):
    closet = dict()
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]] += 1
        else:
            closet[cloth[1]] = 1

    numbers = []
    for number in closet.values():
        numbers.append(number)

    answer = sum(numbers)
    for i in range(2, len(numbers)+1):
        combination = list(combinations(numbers, i))
        for pair in combination:
            temp = 1
            for num in pair:
                temp *= num
            answer += temp

    return answer


# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))