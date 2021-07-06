import sys
sys.stdin = open('sample_input.txt')


def perm(cnt, origin, case, record, result, check):
    if cnt == len(origin):
        result_value = ''.join(case)
        result.append(result_value)
    else:
        for i in range(len(origin)):
            if i not in set(record):
                case.append(origin[i])
                value = ''.join(case)
                if value not in check[cnt]:
                    check[cnt].append(value)
                    perm(cnt+1, origin, case, record + [i], result, check)
                case.pop()


def make_dict(numbers, delta):
    result = dict()

    for number in numbers:
        number_list = list(number)
        decimal = 0
        inc = 1
        for i in range(len(number_list)-1, -1, -1):
            decimal += int(number[i]) * inc
            inc *= delta
        result[number] = decimal

    return result


# main
for tc in range(1, int(input())+1):
    binary = list(input())
    ternary = list(input())

    binary_result = []
    binary_check = [[] for _ in range(len(binary))]
    perm(0, binary, [], [], binary_result, binary_check)
    binary_dict = make_dict(binary_result, 2)

    ternary_result = []
    ternary_check = [[] for _ in range(len(ternary))]
    perm(0, ternary, [], [], ternary_result, ternary_check)
    ternary_dict = make_dict(ternary_result, 3)

    print(binary_dict, ternary_dict)
