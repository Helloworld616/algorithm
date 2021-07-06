import operator


def solution(genres, plays):
    answer = []

    playcounter = dict()  # 장르별 플레이 횟수를 기록할 딕셔너리
    playlist = dict()  # 장르별 플레이 기록을 기록할 딕셔너리

    # 리스트 genres에서 장르를 하나씩 꺼낸다.
    # 장르를 키 값으로 삼고, 장르와 고유번호가 일치하는 플레이 기록을 찾는다.
    # playcounter에는 장르별 총 재생 횟수를,
    # playlist에는 장르별 재생 내역을 저장한다. 재생 내역은 {'고유번호': '재생횟수'} 형태의 딕셔너리이다.
    for i in range(len(genres)):
        if genres[i] not in playcounter:
            playcounter[genres[i]] = plays[i]
            playlist[genres[i]] = {i: plays[i]}
        else:
            playcounter[genres[i]] += plays[i]
            playlist[genres[i]][i] = plays[i]

    # playcounter를 value 값을 기준으로 역순 정렬
    sorted_playcounter = sorted(playcounter.items(), key=operator.itemgetter(1), reverse=True)

    # playlist의 기록을 value 값을 기준으로 역순 정렬
    for genre, record in playlist.items():
        playlist[genre] = sorted(record.items(), key=operator.itemgetter(1), reverse=True)

    # 정렬된 playcounter에서 장르를 하나씩 꺼낸다.
    for counter in sorted_playcounter:
        # 장르의 곡이 1곡보다 많으면 두 곡을 정답에 담는다.
        if len(playlist[counter[0]]) > 1:
            answer.append(playlist[counter[0]][0][0])
            answer.append(playlist[counter[0]][1][0])
        # 예외처리! 이거 안 하면 런타임 에러!!!
        # 장르의 곡이 하나 뿐이면 1곡만 담는다.
        else:
            answer.append(playlist[counter[0]][0][0])

    # 정답 반환
    return answer


# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
# genres = ["classic", "classic", "classic"]
# plays = [500, 600, 150]
genres = ["classic", "pop", "rock", "jazz", "soul"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))