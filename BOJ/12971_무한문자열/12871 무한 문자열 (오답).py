import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

s_set = set(list(s))
t_set = set(list(t))

if len(s_set)==1 and len(t_set)==1 and s_set==t_set:
    print(1)

else:
    if len(s) > len(t):
        long = s
        short = t
    else:
        long = t
        short = s

    if len(long) % len(short) != 0:
        print(0)
    else:
        flag = True
        
        for idx in range(0, len(long)-len(short)+1, len(short)):
            if long[idx:idx+len(short)] != short:
                flag = False
                break
            
        if flag:
            print(1)
        else:
            print(0)
