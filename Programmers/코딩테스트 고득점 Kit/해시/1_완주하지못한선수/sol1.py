# 해시 1 : 완주하지 못한 선수

def solution(participant, completion):
    # 두 리스트를 정렬
    participant.sort()
    completion.sort()

    # 두 리스트를 비교했을 때, 서로 다른 이름이 나왔다면
    # 그 참가자가 바로 미완주한 사람이다!
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 미완주한 사람을 못 찾았을 경우, 마지막 참가자가 미완주한 사람
    return participant[-1]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))