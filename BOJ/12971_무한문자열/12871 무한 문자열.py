import sys

def LCM(num1, num2):
    answer = 0
    for i in range(1, num1*num2+1):
        if i % num1 == 0 and i % num2 == 0:
            answer = i
            break
    return answer


s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

mul_num = LCM(len(s), len(t))

if s*(mul_num//len(s)) == t*(mul_num//len(t)):
    print(1)
else:
    print(0)
