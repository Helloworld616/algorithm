#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#pragma warning(disable:4996)

using namespace std;

void makeGraph(vector<int> *graph, int **map, int* valid, int w, int h); // �׷��� ���� �Լ�
void dfs(vector<int> *graph, int *visit, int vertex); // dfs �Լ�
int component(vector<int> *graph, int *valid, int n); // ���� ����� ������ ��ȯ�ϴ� �Լ�

int main() {
	int w, h;

	/* ���ѷ��� ���� */
	while (1) {
		cin >> w >> h;
		cin.ignore();
		/* �Է� ���� w�� h�� ��� 0�� �� ���ѷ��� ���� */
		if (w == 0 && h == 00) {
			break;
		}

		/* ���� �ٴ��� ������ ������ ������ �迭 map ���� */
		int **map = new int*[h + 2];
		for (int i = 0; i < h + 2; i++) {
			map[i] = new int[w + 2]();
		}

		string field;
		string area = "";

		/* �Է��� ���� 0�� 1�� ������ �迭�� ���� */
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

		/* �׷����� ���� vector ���� */
		vector<int> *graph = new vector<int>[(w * h) + 1];

		/* ������ �ƴ����� üũ�ϴ� �迭 valid ����. ���� ��� 1, ���� �ƴ� ��� 0 ���� */
		int *valid = new int[(w * h) + 1]();

		/* �׷��� ���� */
		makeGraph(graph, map, valid, w, h);

		/* ���� ����� ������ ��ȯ�޾� ��� */
		int result = component(graph, valid, w * h);
		cout << result << endl;
	}
	
	return 0;
}

/* �׷��� ���� �Լ�. ������ �迭 map�� �����ϴ� �� ������ 8������ Ž���� �� ���� ����Ʈ�� �����Ѵ�. */
void makeGraph(vector<int> *graph, int **map, int* valid, int w, int h) {
	int index = 1; // �迭 valid�� �����ϱ� ���� ���� index
	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) {
			/* �������� ���� �߰ߵ� �� �迭 valid�� ���� 1�� �ٲٰ� ���� 8���� Ȯ�� */
			/* 8���� �߿� ���� ���� ��� vector�� �����Ͽ� ���� ����Ʈ�� �ϼ� */
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

/* dfs �Լ�. �湮 ���θ� üũ�ϴ� �迭 visit�� �̿��Ͽ� �湮���� �ʴ� vertex�� �湮�Ѵ�.  */
void dfs(vector<int> *graph, int *visit, int vertex) {
	/* �湮�� ���� visit�� ���� 1�� �ٲپ �湮�ߴٴ� ����� ����� */
	visit[vertex] = 1;
	for (int v : graph[vertex]) {
		/* visit�� ���� 0�̸� �湮���� ���� ���̹Ƿ� dfs�� ȣ���Ͽ� �湮�Ѵ� */
		if (visit[v] == 0) {
			dfs(graph, visit, v);
		}
	}
}

/* ���� ����� ������ ���ϴ� �Լ� */
int component(vector<int> *graph, int *valid, int n) {
	/* �湮 ���θ� üũ�ϴ� �迭 visit�� �����Ͽ� 0���� �ʱ�ȭ */
	/* visit�� ���� �湮���� ��쿡�� 1, �湮���� �ʾ��� ��쿡�� 0�̴� */
	int *visit = new int[n + 1]();
	
	int count = 0; // �������� ������ ��� ���� count

	/* ��������Ʈ�� ������ ���͸� ���ʴ�� Ž���Ѵ�.*/
	for (int i = 1; i <= n; i++) {
		/* valid�� ���� 1�̰�, �湮���� �ʴ� vertex�� ���� ��� dfs�� ȣ���ϰ� ���� ����� ������ 1 �ø��� */
		/* valid�� ���� 0�̰ų�, �湮�� ��쿡�� dfs�� ȣ����� �����Ƿ� ��������� ������� ���� ��ҵ��� dfs�� ȣ���Ų�� */
		if (valid[i] == 1 && visit[i] == 0) {
			dfs(graph, visit, i);
			count++;
		}
	}
	return count;
}