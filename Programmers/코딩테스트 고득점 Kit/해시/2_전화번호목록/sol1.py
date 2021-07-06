# 해시 2 : 전화번호 목록

def solution(phone_book):
    # 전화번호부 정렬
    # 이렇게 전처리를 하면 앞 숫자가 비슷한 것들끼리 모이게 된다!
    phone_book.sort()

    # 전화번호부를 한 바퀴 돌면서 양 옆의 두 번호를 서로 비교하자!
    for i in range(len(phone_book)-1):
        # 두 번호 중 긴 번호와 짧은 번호 가려내기
        if len(phone_book[i]) > len(phone_book[i+1]):
            long_num = phone_book[i]
            short_num = phone_book[i+1]
        else:
            long_num = phone_book[i + 1]
            short_num = phone_book[i]
        # 짧은 번호가 긴 번호의 접두사인 경우 False 반환
        if short_num == long_num[:len(short_num)]:
            return False

    # 중간에 False 반환이 안 되었으면 True 반환
    return True


# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))
