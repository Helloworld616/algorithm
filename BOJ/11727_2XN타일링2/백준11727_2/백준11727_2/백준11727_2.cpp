#include<iostream>

using namespace std;

int main() {
	int num;
	unsigned long answer;
	cin >> num;
	unsigned long* arr = new unsigned long[num]();
	arr[0] = 1; // ù ��° Base Case
	arr[1] = 3; // �� ��° Base Case
	if (num == 1) answer = arr[0]; // n�� 1�� �� ù ��° Base Case ��ȯ
	else if (num == 2) answer = arr[1]; // n�� 2�� �� �� ��° Base Case ��ȯ
	/* n�� 3 �̻��� �� DP ���� */
	else {
		/* ���� ������ �̿��� ������ ��� */
		for (int i = 2; i < num; i++) {
			/* ���⿡�� �ٷ� 10007�� ������ �� �������� �־��ش� */
			/* �̷��� ���� ������ 10007�� ���������� �� ���� unsigned long�� Ŀ�� �������� Ŀ�� �����÷ο찡 �߻��Ѵ� */
			arr[i] = (arr[i - 1] + 2 * arr[i - 2]) % 10007;
		}
		/* ������ �迭 ���� �ٷ� ������ �����̴� */
		answer = arr[num - 1];
	}
	cout << answer;
	return 0;
}