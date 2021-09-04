// bfs 함수
function bfs(graph, visited, distances) {
  let queue = [[1, 1]]  // 큐 생성 및 초기화
  visited[1] = true  // 방문체크
  
  // bfs 탐색 시작
  while (true) {
      // 큐가 비게 되면 탐색 중지
      if (queue.length === 0) {
          break
      }
      
      // 큐에서 인덱스와 거리 추출
      const info = queue.shift()
      const idx = info[0]
      const distance = info[1]
      
      // 그래프를 탐색하여 방문하지 않은 노드까지의 거리를 입력
      for (let i = 0; i < graph[idx].length; i++) {
          if (!visited[graph[idx][i]]) {
              visited[graph[idx][i]] = true
              distances[graph[idx][i]] = distance
              queue.push([graph[idx][i], distance + 1])
          }
      }
  }
}


// 정답 함수
function solution(n, vertex) {
  let answer = 0;  // 정답
  let graph = []  // 그래프
  let distances = []  // 거리 배열
  let visited = []  // 방문 배열
  
  // 그래프, 거리 배열, 방문 배열 초기화
  for (let i = 0; i <= n; i++) {
      graph.push([])
      distances.push(0)
      visited.push(false)
  }
  
  // 노드 연결 정보를 보고 그래프를 채우기
  vertex.forEach(el => {
    graph[el[0]].push(el[1])
    graph[el[1]].push(el[0])
  })
  
  // bfs 탐색
  bfs(graph, visited, distances)
  
  // 1번 노드에서 가장 먼 거리에 있는 노드들의 갯수를 세기
  distances.forEach(el => {
      if (el === Math.max(...distances)) {
          answer++
      }
  })
  
  return answer;  // 정답 반환
}