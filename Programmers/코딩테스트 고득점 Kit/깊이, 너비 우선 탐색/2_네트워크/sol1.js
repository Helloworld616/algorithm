/* DFS 함수 */
function dfs(computers, idx, visited) {
  visited[idx] = true // 방문체크
  
  /* 연결되어 있고, 방문하지 않은 노드가 있으면 DFS 실행 */
  computers[idx].forEach((number, i) => {
      if (number === 1 && !visited[i]) {
          dfs(computers, i, visited)
      }
  })
}

/* 솔루션 함수 */
function solution(n, computers) {
  var answer = 0 // 정답 초기화
  let visited = Array(n).fill(false) // 방문배열 초기화
  
  /* computers를 탐색하면서 연결요소 구하기 */
  computers.forEach((computer, idx) => {
      if (!visited[idx]) {
          dfs(computers, idx, visited)
          answer++
      }
  })
  
  return answer;
}