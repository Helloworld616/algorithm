# 교수님 해설

P = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
     '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def scan(barcode):
    for i in range(N):
        for j in range(M-1, 0, -1):
            if barcode[i][j] == '0':
                continue
            else:
                decrypt_numbers = []
                # i row의 k ~ k+7에 해당하는 바코드를 읽어서 대응하는 숫자로 바꾸면 된다.
                for k in range(j-56+1, j, 7):
                    decrypt_numbers.append(P[barcode[i]][k:k+7])

                odd_sum = 0
                even_sum = 0

                for idx in range(len(decrypt_numbers)):
                    if idx % 2:
                        odd_sum += decrypt_numbers[idx]
                    else:
                        even_sum += decrypt_numbers[idx]

                if (odd_sum * 3 + even_sum) % 10:
                    return 0
                else:
                    return odd_sum + even_sum



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    barcode = [input() for _ in range(N)]
    print("#{} {}".format(tc, scan(barcode)))