# 해쉬 3 : 위장


def solution(clothes):
    # 옷을 종류 별로 분류
    closet = dict()
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]] += 1
        else:
            closet[cloth[1]] = 1

    # 경우의 수 나누기
    # 한 종류의 옷이 n벌 주어졌을 때, 그 종류의 옷을 입는 경우는 (n+1)가지이다!
    # 옷을 0벌 입을 때, 1벌 입을 때, 2벌 입을 때, ........ , n벌 입을 때
    # 결국 (옷 갯수 + 1)을 계속 곱해나가면 되는 것이다!!!
    answer = 1
    for number in closet.values():
        answer *= number + 1

    # 최소한 한 벌은 입으므로, 아무것도 안 입는 경우의 수를 빼서 반환
    return answer - 1


# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))