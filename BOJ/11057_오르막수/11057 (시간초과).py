import sys

n = int(sys.stdin.readline())

number = 0
answer = 0

while len(str(number)) <= n:
    number_list = list(map(int, list(str(number))))
    copy_list = number_list[:]

    copy_list.sort()
    
    for i in range(len(copy_list)-1):
        for j in range(i, len(copy_list)):
            if copy_list[i] > copy_list[j]:
                temp = copy_list[i]
                copy_list[i] = copy_list[j]
                copy_list[j] = temp
                
    if number_list == copy_list :
        answer += 1
    number += 1

print(answer % 10007)
    
        
