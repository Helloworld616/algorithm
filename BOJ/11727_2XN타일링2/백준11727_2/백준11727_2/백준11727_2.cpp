#include<iostream>

using namespace std;

int main() {
	int num;
	unsigned long answer;
	cin >> num;
	unsigned long* arr = new unsigned long[num]();
	arr[0] = 1; // 첫 번째 Base Case
	arr[1] = 3; // 두 번째 Base Case
	if (num == 1) answer = arr[0]; // n이 1일 때 첫 번째 Base Case 반환
	else if (num == 2) answer = arr[1]; // n이 2일 때 두 번째 Base Case 반환
	/* n이 3 이상일 때 DP 실행 */
	else {
		/* 과거 값들을 이용한 순차적 계산 */
		for (int i = 2; i < num; i++) {
			/* 여기에서 바로 10007로 나누어 그 나머지를 넣어준다 */
			/* 이렇게 하지 않으면 10007로 나누어지기 전 값이 unsigned long의 커버 범위보다 커서 오버플로우가 발생한다 */
			arr[i] = (arr[i - 1] + 2 * arr[i - 2]) % 10007;
		}
		/* 마지막 배열 값이 바로 문제의 정답이다 */
		answer = arr[num - 1];
	}
	cout << answer;
	return 0;
}