'''

1. 내장함수(x)
2. 직접 짜기
3. 재귀로 짜기

'''

# 1. 반복문
word = 'abcdef'
reversed_word = ''

for i in range(len(word)-1, -1, -1):
    reversed_word += word[i]

print(reversed_word)


# 2. 재귀
def reversing(word, idx):
    if idx == 0:
        return word[idx]
    return word[idx] + reversing(word, idx-1)

word = 'abcdef'
reversed_word = reversing(word, len(word)-1)

print(reversed_word)


# 3. 리스트 활용
word = 'abcdef'
word_list = list(word)

for i in range(len(word_list)//2):
    word_list[i], word_list[len(word_list)-i-1] = word_list[len(word_list)-i-1], word_list[i]

print(''.join(word_list))

