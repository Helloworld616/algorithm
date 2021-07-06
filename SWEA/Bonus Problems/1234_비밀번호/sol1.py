import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N, string = input().split()
    N = int(N)
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            l_idx = i - 1
            r_idx = i + 2
            while True:
                if l_idx >= 0 and r_idx <= len(string)-1 and string[l_idx] == string[r_idx]:
                    l_idx -= 1
                    r_idx += 1
                else:
                    l_idx += 1
                    r_idx -= 1
                    break
            string = string[0:l_idx] + string[r_idx+1:len(string)]
            i = 0
        i += 1
    print('#{} {}'.format(tc, string))




