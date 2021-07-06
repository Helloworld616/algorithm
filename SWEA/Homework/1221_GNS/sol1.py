import sys
sys.stdin = open("GNS_test_input.txt")


def Insertion_Sort(strings, numbers):
    for i in range(len(strings)-1):
        for j in range(i + 1, len(strings)):
            if numbers[strings[i]] > numbers[strings[j]]:
                strings[i], strings[j] = strings[j], strings[i]


T = int(input())
numbers = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}


for tc in range(1, T+1):
    N, L = input().split()
    strings = input().split()
    Insertion_Sort(strings, numbers)
    print(N)
    for string in strings:
        print(string, end = ' ')

