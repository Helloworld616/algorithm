#include<iostream>

using namespace std;

int tile(int n);

int main() {
	int num, answer;
	cin >> num;
	answer = tile(num);
	answer %= 10007;
	cout << answer;
	return 0;
}

int tile(int n) {
	if (n == 1) return 1;
	if (n == 2) return 3;
	return tile(n - 1) + 2*tile(n - 2);
}