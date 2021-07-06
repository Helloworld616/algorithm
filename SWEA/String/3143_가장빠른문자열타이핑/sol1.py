# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    string, pat = input().split()
    idx = 0
    cnt = 0
    while len(string) >= len(pat) and pat in string:
        if pat == string[idx:idx+len(pat)]:
            string = string[idx+len(pat):len(string)]
            idx = 0
        else:
            idx += 1
        cnt += 1
    if len(string) > 0:
        cnt += len(string)
    print("#{} {}".format(tc, cnt))