#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

void dfs(vector<int> *graph, int *visit, int vertex); // dfs 함수
int component(vector<int> *graph, int n); // 연결요소의 개수를 구하는 함수

int main() {
	int n, m, answer;

	/* vertex의 개수 n와 edge의 개수 m 입력 */
	cin >> n >> m;

	/* 그래프를 만들 vector 생성 */
	vector<int> *graph = new vector<int>[n + 1];

	/* 출발지와 도착지 vector에 원소들을 추가하여 인접리스트를 생성 */
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		/* 무방향 그래프는 양방향성을 가지므로 출발지와 도착지에 모두 연결해주어야 한다 */
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	/* 연결 요소의 개수를 반환받아 출력 */
	answer = component(graph, n);
	cout << answer;

	return 0;
}

/* dfs 함수. 방문 여부를 체크하는 배열 visit를 이용하여 방문하지 않는 vertex만 방문한다.  */
void dfs(vector<int> *graph, int *visit, int vertex) {
	/* 방문한 순간 visit의 값을 1로 바꾸어서 방문했다는 기록을 남긴다 */
	visit[vertex] = 1;
	for (int v : graph[vertex]) {
		/* visit의 값이 0이면 방문하지 않은 것이므로 dfs를 호출하여 방문한다 */
		if (visit[v] == 0) {
			dfs(graph, visit, v);
		}
	}

}

/* 연결 요소의 개수를 구하는 함수 */
int component(vector<int> *graph, int n) {
	/* 방문 여부를 체크하는 배열 visit를 생성하여 0으로 초기화 */
	/* visit의 값은 방문했을 경우에는 1, 방문하지 않았을 경우에는 0이다 */
	int *visit = new int[n + 1](); 

	int count = 0; // 연결요소의 개수를 담는 변수 count

	/* 인접리스트가 구현된 벡터를 차례대로 탐색한다.*/
	for (int i = 1; i <= n; i++) {
		/* 방문하지 않는 vertex가 나온 경우 dfs를 호출하고 연결 요소의 개수를 1 늘린다 */
		/* 방문한 경우에는 dfs가 호출되지 않으므로 결과적으로 연결되지 않은 요소들이 dfs를 호출시킨다 */
		if (visit[i] == 0) {
			dfs(graph, visit, i);
			count++;
		}
	}
	return count;
}