#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>

using namespace std;

int minimumCost(int *value, int n); // 최소 비용을 구해서 반환하는 함수

int main() {
	int n;

	/* 카드의 개수 입력 받기 */
	cin >> n;
	cin.ignore();

	int *value = new int[n + 1]();
	string price;
	string p = "";

	/* 카드의 금액 입력 받기 */
	getline(cin, price);
	int count = 1;
	int len = price.length();
	for (int i = 0; i < len; i++) {
		if (price.at(i) == ' ') {
			value[count] = stoi(p);
			p = "";
			count++;
		}
		else {
			p += price.at(i);
		}
	}
	value[count] = stoi(p);
	p = "";

	/* 최소 비용을 구한 뒤 출력 */
	int maxCost = minimumCost(value, n);

	cout << maxCost;

	return 0;
}

/* 최소 비용을 구하는 함수. 최소 비용을 구할 때에는 이차원 배열을 활용한다. */
int minimumCost(int *value, int n) {
	/* 최소 비용을 저장하는 이차원 배열 cost 생성 */
	int **cost = new int*[n + 1];
	for (int i = 0; i < n + 1; i++) {
		cost[i] = new int[n + 1]();
	}

	/* base case 채우기 */
	/* 1개짜리 카드팩만으로 도출할 수 있는 비용 채우기  */
	for (int i = 1; i <= n; i++) {
		cost[1][i] = i * value[1];
	}

	/* N개의 카드를 갖기 위해 지불할 수 있는 최소 비용 구하기 */
	/* 3개의 값을 비교해서 가장 작은 값을 배열에 저장한다. */
	/* 1. (i-1)개짜리 카드팩만 구입했을 때의 비용 */
	/* 2. i개짜리 카드팩만 구입했을 때의 비용    */
	/* 3. 1 + 2 + ....+ (i-1) + i = N을 만족하는 카드팩들을 섞어서 구입했을 때의 비용 */
	/* 이 과정을 거쳐 배열의 맨 마지막 칸에는 최소 비용이 저장된다 */
	for (int i = 2; i <= n; i++) { // 1개짜리 카드팩의 비용을 채웠으므로 i = 2부터 시작
		for (int j = 1; j <= n; j++) {
			/* (i-1)개짜리 카드팩이었을 때의 비용을 넘겨받음 */
			cost[i][j] = cost[i - 1][j];
			/* (i-1)개짜리 카드팩과 i개짜리 카드팩의 비용을 비교해서 큰 값으로 교체 */
			if (j == i) {
				if (value[i] < cost[i][j]) {
					cost[i][j] = value[i];
				}
			}
			/* 1 + 2 + ....+ (i-1) + i = N을 만족하는 카드팩 조합의 비용과 현재 비용을 비교해서 작은 값으로 교체 */
			else if (j > i) {
				for (int k = 1; k <= j / 2; k++) {
					int temp = cost[i][k] + cost[i][j - k];
					if (temp < cost[i][j]) {
						cost[i][j] = temp;
					}
				}
			}
		}
	}
	return cost[n][n]; // 최소 비용을 반환
}