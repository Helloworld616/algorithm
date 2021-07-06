#ifndef _CRT_SECURE_NO_WARNINGS 
#define _CRT_SECURE_NO_WARNINGS 
#endif
#include <stdio.h>

int main(void) {
	int m, n, m1, m2, max, count, num, compare, decide;
	count = num = 0;
	scanf("%d %d", &m, &n);
	max = m;
	int l[1001] = { 0, };
	int check[1001] = { 0, };
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &m1, &m2);
		if (m1 > max) {
			max = m1;
		}
		if (m2 > max) {
			max = m2;
		}
		if (check[m1] == 0) {
			check[m1] = 1;
			num++;
		}
		if (check[m2] == 0) {
			check[m2] = 1;
			num++;
		}
		if (l[m1] == 0 and l[m2] == 0) {
			count++;
			l[m1] = count;
			l[m2] = count;
		}
		else if (l[m1] == 0 and l[m2] != 0) {
			l[m1] = l[m2];
		}
		else if (l[m1] != 0 and l[m2] == 0) {
			l[m2] = l[m1];
		}
		else {
			if (l[m1] == l[m2]) continue;
			else {
				count--;
				if (l[m1] < l[m2]) {
					decide = l[m1];
					compare = l[m2];
				}
				if (l[m1] > l[m2]) {
					decide = l[m2];
					compare = l[m1];
				}
				for (int j = 1; j < m + 1; j++) {
					if (l[j] == compare) {
						l[j] = decide;
					}

				}

			}

		}
	}
	if (n == 0) {
		printf("%d", m);
	}
	else {
		int zero = 0;
		for (int i = 1; i <= max; i++) {
			if (l[i] == 0 && check[i] == 1) zero++;
		}
		printf("%d", count+zero+(m-num));
	}
}