import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    N, G = map(int, input().split())
    numbers = list(map(int, input().split()))

    sequence = []
    for idx in range(len(numbers)):
        if not numbers[idx] % G:
            sequence.append(numbers[idx])

    factors = []
    for num in sequence:
        factor = []
        for n in range(1, num+1):
            if not num % n:
                factor.append(n)
        factors.append(factor)
    # print(factors)

    counter = [0] * len(sequence)
    for idx in range(len(sequence)):
        if sequence[idx] == G:
            counter[idx] += 1
    # print(counter)

    for i in range(1, len(sequence)):
        exp = 0
        plus = 0
        delta = 1
        for j in range(i):
            if max(set(factors[i]) & set(factors[j])) == G:
                plus += 2 ** exp
            else:
                # print(delta)
                plus += 2 ** exp - delta
                # delta += 1
            exp += 1
        counter[i] += plus
    # print(counter)

    total = 0
    for cnt in counter:
        total += cnt

    print('#{} {}'.format(tc, total))



