#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#pragma warning(disable:4996)

using namespace std;

void makeGraph(vector<int> *graph, int **map, int* valid, int w, int h); // 그래프 생성 함수
void dfs(vector<int> *graph, int *visit, int vertex); // dfs 함수
int component(vector<int> *graph, int *valid, int n); // 연결 요소의 갯수를 반환하는 함수

int main() {
	int w, h;

	/* 무한루프 생성 */
	while (1) {
		cin >> w >> h;
		cin.ignore();
		/* 입력 받은 w와 h가 모두 0일 때 무한루프 종료 */
		if (w == 0 && h == 00) {
			break;
		}

		/* 섬과 바다의 지형을 저장할 이차원 배열 map 생성 */
		int **map = new int*[h + 2];
		for (int i = 0; i < h + 2; i++) {
			map[i] = new int[w + 2]();
		}

		string field;
		string area = "";

		/* 입력을 받은 0과 1을 이차원 배열에 저장 */
		for (int i = 1; i <= h; i++) {
			getline(cin, field);
			int count = 1;
			int len = field.length();
			for (int j = 0; j < len; j++) {
				if (field.at(j) == ' ') {
					map[i][count] = stoi(area);
					area = "";
					count++;
				}
				else {
					area += field.at(j);
				}
			}
			map[i][count] = stoi(area);
			area = "";
		}

		/* 그래프를 만들 vector 생성 */
		vector<int> *graph = new vector<int>[(w * h) + 1];

		/* 섬인지 아닌지를 체크하는 배열 valid 생성. 섬일 경우 1, 섬이 아닐 경우 0 저장 */
		int *valid = new int[(w * h) + 1]();

		/* 그래프 생성 */
		makeGraph(graph, map, valid, w, h);

		/* 연결 요소의 개수를 반환받아 출력 */
		int result = component(graph, valid, w * h);
		cout << result << endl;
	}
	
	return 0;
}

/* 그래프 생성 함수. 이차원 배열 map에 존재하는 각 원소의 8방향을 탐색한 뒤 인접 리스트를 생성한다. */
void makeGraph(vector<int> *graph, int **map, int* valid, int w, int h) {
	int index = 1; // 배열 valid에 접근하기 위한 변수 index
	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) {
			/* 지도에서 섬이 발견될 때 배열 valid의 값을 1로 바꾸고 섬의 8방향 확인 */
			/* 8방향 중에 섬이 있을 경우 vector에 연결하여 인접 리스트를 완성 */
			if (map[i][j] == 1) {
				valid[index] = 1;
				if (map[i - 1][j - 1] == 1) {
					graph[index].push_back(index - (w + 1));
				}
				if (map[i - 1][j] == 1) {
					graph[index].push_back(index - w);
				}
				if (map[i - 1][j + 1] == 1) {
					graph[index].push_back(index - (w - 1));
				}
				if (map[i][j - 1] == 1) {
					graph[index].push_back(index - 1);
				}
				if (map[i][j + 1] == 1) {
					graph[index].push_back(index + 1);
				}
				if (map[i + 1][j - 1] == 1) {
					graph[index].push_back(index + (w - 1));
				}
				if (map[i + 1][j] == 1) {
					graph[index].push_back(index + w);
				}
				if (map[i + 1][j + 1] == 1) {
					graph[index].push_back(index + (w + 1));
				}
			}
			index++;
		}
	}
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
int component(vector<int> *graph, int *valid, int n) {
	/* 방문 여부를 체크하는 배열 visit를 생성하여 0으로 초기화 */
	/* visit의 값은 방문했을 경우에는 1, 방문하지 않았을 경우에는 0이다 */
	int *visit = new int[n + 1]();
	
	int count = 0; // 연결요소의 개수를 담는 변수 count

	/* 인접리스트가 구현된 벡터를 차례대로 탐색한다.*/
	for (int i = 1; i <= n; i++) {
		/* valid의 값이 1이고, 방문하지 않는 vertex가 나온 경우 dfs를 호출하고 연결 요소의 개수를 1 늘린다 */
		/* valid의 값이 0이거나, 방문한 경우에는 dfs가 호출되지 않으므로 결과적으로 연결되지 않은 요소들이 dfs를 호출시킨다 */
		if (valid[i] == 1 && visit[i] == 0) {
			dfs(graph, visit, i);
			count++;
		}
	}
	return count;
}