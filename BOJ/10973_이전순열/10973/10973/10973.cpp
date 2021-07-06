#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

void transform(vector<int> &sequence, int n); // 이전 순열을 구해서 출력하는 함수

int main() {
	int n;
	/* 순열의 길이 입력 받기 */
	cin >> n;
	cin.ignore();

	vector<int> sequence;
	string numbers;
	string number = "";

	/* 순열 입력 받기. 입력 받은 후 벡터에 담는다. */
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

	/* 이전 순열을 구해서 출력하기 */
	transform(sequence, n);

	return 0;
}

/* 이전 순열을 구해서 출력하는 함수 */
void transform(vector<int> &sequence, int n) {
	vector<int> box;
	/* 순열의 내림차순 구간 길이를 측정하는 변수 count */
	int count = 1;

	/* 내림차순 여부를 끝에서부터 점검한다. 점검이 끝나면 sequence로부터 수를 빼서 box에 담는다. */
	/* 앞의 수가 현재 수보다 작을 경우 루프를 계속하고, 그 외의 경우 루프를 빠져나온다. */
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
	
	/* count의 값이 순열의 길이와 같으면 -1 출력 */
	if (count == n) {
		cout << -1;
	}
	/* 아닐 경우 이전 순열을 구해서 출력 */
	else {
		vector<int> candidate;

		/* 남은 순열의 마지막 수보다 작은 수들은 교환 후보이다. candidate에 담는다. */
		for (int b : box) {
			if (b < sequence.back()) {
				candidate.push_back(b);
			}
		}

		/* candidate를 정렬한다. 그 후 가장 마지막에 있는 수(최댓값)을 temp에 저장한다. */
		sort(candidate.begin(), candidate.end());
		int temp = candidate.back();

		/* 순열에서 끝 수를 빼서 box에 담고 temp를 추가해준다. */
		box.push_back(sequence.back());
		sequence.pop_back();
		sequence.push_back(temp);

		/* box를 정렬한다. */
		sort(box.begin(), box.end(), greater<>());
		/* box의 수들을 순열에 순서대로 붙인다. */
		for (int b : box) {
			if (b != temp) {
				sequence.push_back(b);
			}
		}
		/* 완성된 순열을 출력한다. */
		for (int s : sequence) {
			printf("%d ", s);
		}
	}

}