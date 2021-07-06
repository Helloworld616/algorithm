#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

void dfs(vector<int> *graph, int *visit, int vertex); // dfs �Լ�
int component(vector<int> *graph, int n); // �������� ������ ���ϴ� �Լ�

int main() {
	int n, m, answer;

	/* vertex�� ���� n�� edge�� ���� m �Է� */
	cin >> n >> m;

	/* �׷����� ���� vector ���� */
	vector<int> *graph = new vector<int>[n + 1];

	/* ������� ������ vector�� ���ҵ��� �߰��Ͽ� ��������Ʈ�� ���� */
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		/* ������ �׷����� ����⼺�� �����Ƿ� ������� �������� ��� �������־�� �Ѵ� */
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	/* ���� ����� ������ ��ȯ�޾� ��� */
	answer = component(graph, n);
	cout << answer;

	return 0;
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
int component(vector<int> *graph, int n) {
	/* �湮 ���θ� üũ�ϴ� �迭 visit�� �����Ͽ� 0���� �ʱ�ȭ */
	/* visit�� ���� �湮���� ��쿡�� 1, �湮���� �ʾ��� ��쿡�� 0�̴� */
	int *visit = new int[n + 1](); 

	int count = 0; // �������� ������ ��� ���� count

	/* ��������Ʈ�� ������ ���͸� ���ʴ�� Ž���Ѵ�.*/
	for (int i = 1; i <= n; i++) {
		/* �湮���� �ʴ� vertex�� ���� ��� dfs�� ȣ���ϰ� ���� ����� ������ 1 �ø��� */
		/* �湮�� ��쿡�� dfs�� ȣ����� �����Ƿ� ��������� ������� ���� ��ҵ��� dfs�� ȣ���Ų�� */
		if (visit[i] == 0) {
			dfs(graph, visit, i);
			count++;
		}
	}
	return count;
}