#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

void transform(vector<int> &sequence, int n); // ���� ������ ���ؼ� ����ϴ� �Լ�

int main() {
	int n;
	/* ������ ���� �Է� �ޱ� */
	cin >> n;
	cin.ignore();

	vector<int> sequence;
	string numbers;
	string number = "";

	/* ���� �Է� �ޱ�. �Է� ���� �� ���Ϳ� ��´�. */
	getline(cin, numbers);
	int len = numbers.length();
	for (int i = 0; i < len; i++) {
		if (numbers.at(i) == ' ') {
			sequence.push_back(stoi(number));
			number = "";
		}
		else {
			number += numbers.at(i);
		}
	}
	sequence.push_back(stoi(number));
	number = "";

	/* ���� ������ ���ؼ� ����ϱ� */
	transform(sequence, n);

	return 0;
}

/* ���� ������ ���ؼ� ����ϴ� �Լ� */
void transform(vector<int> &sequence, int n) {
	vector<int> box;
	/* ������ �������� ���� ���̸� �����ϴ� ���� count */
	int count = 1;

	/* �������� ���θ� ���������� �����Ѵ�. ������ ������ sequence�κ��� ���� ���� box�� ��´�. */
	/* ���� ���� ���� ������ ���� ��� ������ ����ϰ�, �� ���� ��� ������ �������´�. */
	for (int i = n - 1; i > 0; i--) {
		if (sequence[i] > sequence[i - 1]) {
			box.push_back(sequence.back());
			sequence.pop_back();
			count++;
		}
		else {
			box.push_back(sequence.back());
			sequence.pop_back();
			break;
		}
	}
	
	/* count�� ���� ������ ���̿� ������ -1 ��� */
	if (count == n) {
		cout << -1;
	}
	/* �ƴ� ��� ���� ������ ���ؼ� ��� */
	else {
		vector<int> candidate;

		/* ���� ������ ������ ������ ���� ������ ��ȯ �ĺ��̴�. candidate�� ��´�. */
		for (int b : box) {
			if (b < sequence.back()) {
				candidate.push_back(b);
			}
		}

		/* candidate�� �����Ѵ�. �� �� ���� �������� �ִ� ��(�ִ�)�� temp�� �����Ѵ�. */
		sort(candidate.begin(), candidate.end());
		int temp = candidate.back();

		/* �������� �� ���� ���� box�� ��� temp�� �߰����ش�. */
		box.push_back(sequence.back());
		sequence.pop_back();
		sequence.push_back(temp);

		/* box�� �����Ѵ�. */
		sort(box.begin(), box.end(), greater<>());
		/* box�� ������ ������ ������� ���δ�. */
		for (int b : box) {
			if (b != temp) {
				sequence.push_back(b);
			}
		}
		/* �ϼ��� ������ ����Ѵ�. */
		for (int s : sequence) {
			printf("%d ", s);
		}
	}

}