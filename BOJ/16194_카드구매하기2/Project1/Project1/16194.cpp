#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>

using namespace std;

int minimumCost(int *value, int n); // �ּ� ����� ���ؼ� ��ȯ�ϴ� �Լ�

int main() {
	int n;

	/* ī���� ���� �Է� �ޱ� */
	cin >> n;
	cin.ignore();

	int *value = new int[n + 1]();
	string price;
	string p = "";

	/* ī���� �ݾ� �Է� �ޱ� */
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

	/* �ּ� ����� ���� �� ��� */
	int maxCost = minimumCost(value, n);

	cout << maxCost;

	return 0;
}

/* �ּ� ����� ���ϴ� �Լ�. �ּ� ����� ���� ������ ������ �迭�� Ȱ���Ѵ�. */
int minimumCost(int *value, int n) {
	/* �ּ� ����� �����ϴ� ������ �迭 cost ���� */
	int **cost = new int*[n + 1];
	for (int i = 0; i < n + 1; i++) {
		cost[i] = new int[n + 1]();
	}

	/* base case ä��� */
	/* 1��¥�� ī���Ѹ����� ������ �� �ִ� ��� ä���  */
	for (int i = 1; i <= n; i++) {
		cost[1][i] = i * value[1];
	}

	/* N���� ī�带 ���� ���� ������ �� �ִ� �ּ� ��� ���ϱ� */
	/* 3���� ���� ���ؼ� ���� ���� ���� �迭�� �����Ѵ�. */
	/* 1. (i-1)��¥�� ī���Ѹ� �������� ���� ��� */
	/* 2. i��¥�� ī���Ѹ� �������� ���� ���    */
	/* 3. 1 + 2 + ....+ (i-1) + i = N�� �����ϴ� ī���ѵ��� ��� �������� ���� ��� */
	/* �� ������ ���� �迭�� �� ������ ĭ���� �ּ� ����� ����ȴ� */
	for (int i = 2; i <= n; i++) { // 1��¥�� ī������ ����� ä�����Ƿ� i = 2���� ����
		for (int j = 1; j <= n; j++) {
			/* (i-1)��¥�� ī�����̾��� ���� ����� �Ѱܹ��� */
			cost[i][j] = cost[i - 1][j];
			/* (i-1)��¥�� ī���Ѱ� i��¥�� ī������ ����� ���ؼ� ū ������ ��ü */
			if (j == i) {
				if (value[i] < cost[i][j]) {
					cost[i][j] = value[i];
				}
			}
			/* 1 + 2 + ....+ (i-1) + i = N�� �����ϴ� ī���� ������ ���� ���� ����� ���ؼ� ���� ������ ��ü */
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
	return cost[n][n]; // �ּ� ����� ��ȯ
}