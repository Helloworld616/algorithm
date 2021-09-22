//  bfs 함수
function bfs(begin, target, words) {
  let queue = []  // 큐 생성
  let visited = []  // 방문 배열 생성
  let ans = 0  // 정답 초기화
  let cnt = 0  // 글자 갯수 차이 초기화
  
  // 방문 배열 초기화
  for (let i = 0; i < words.length; i++) {
      visited.push(false)
  }
  
  // 글자가 하나만 다른 단어들을 모두 큐에 넣는다.
  // 큐에 넣은 단어들은 방문 체크한다.
  words.forEach((el, idx) => {
      cnt = 0
      for (let i = 0; i < el.length; i++) {
          if (begin[i] !== el[i]) {
              cnt++
          }
      }
      
      if (cnt === 1) {
          queue.push([el, 1])
          visited[idx] = true
      }
  })
  
  // bfs 실행
  while (true) {
      if (queue.length === 0) {
          break
      }
      
      let info = queue.shift()  // 큐에서 원소를 꺼냄
      let word = info[0]  // 단어 꺼내기
      ans = info[1]  // 정답 꺼내기
      
      // 단어가 target과 같으면 바로 정답 반환
      if (word === target) {
          return ans
      }
      
      // 글자가 하나만 다른 단어들을 모두 큐에 넣는다.
      // 큐에 넣은 단어들은 방문 체크한다.
      words.forEach((el, idx) => {
          if (!visited[idx]) {
              cnt = 0
              for (let i = 0; i < el.length; i++) {
                  if (word[i] !== el[i]) {
                      cnt++
                  }
              }
              
              if (cnt === 1) {
                  queue.push([el, ans + 1])
                  visited[idx] = true
              }
          }
      })
  }
  
  // 단어들을 모두 체크했는데도 target이 되지 못할 경우 0을 반환
  return 0
}

// 솔루션 함수
function solution(begin, target, words) {
  let answer = 0  // 정답 초기화
  let flag = true  // 플래그 변수 초기화
  
  // 1. 만약 begin과 target이 같다면 바로 answer 반환
  if (begin === target) {
      return answer
  }
  
  // 2. target이 words에 없는 경우에도 바로 answer 반환
  words.forEach(el => {
      if (target === el) {
          flag = false
      }
  })
  
  if (flag) {
      return answer
  }
  
  // 위 두 경우를 벗어날 경우 bfs 탐색을 통해 답을 찾아낸다.
  answer = bfs(begin, target, words)
  
  return answer  // 정답 반환
}