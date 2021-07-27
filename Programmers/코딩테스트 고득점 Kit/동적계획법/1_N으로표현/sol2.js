// 효율성을 더 높인 코드. 처음부터 집합을 사용하여 불필요한 중복 제거 연산을 뺐다.

function solution(N, number) {
  let answer = -1;  // 정답 초기화
  let dp = [];  // dp 배열 생성
  
  /* N과 number가 같으면 바로 1을 반환 */
  if (N === number) {
      return 1;
  }
  
  /* 기본값을 가진 이차원 배열 생성 ex) [[7], [77], [777], ..., [77777777]] */
  for (let i = 1; i <= 8; i++) {
      let set = new Set([Number(String(N).repeat(i))]);
      dp.push(set);
  }
  
  /* dp 연산 시작. 인덱스 합이 8이 되는 원소끼리 계산 ex) (dp[1], dp[7]), (dp[2], dp[6]) */
  for (let i = 1; i < 8; i++) {
      for (let j = 0; j < i; j++) {
          dp[j].forEach(el1 => {
              dp[i-j-1].forEach(el2 => {
                  dp[i].add(el1 - el2);
                  dp[i].add(el1 + el2);
                  dp[i].add(el1 * el2);
                  if (el2 != 0) {  // 예외처리 필수! 안 할 경우 에러 남!
                      dp[i].add(parseInt(el1 / el2));
                  }
              })
          })
      }
      
      /* 계산된 값에서 number 가 있을 경우 정답 갱신. 아닐 경우 다음 연산 수행. */
      if (dp[i].has(number)) {
          answer = i + 1;
          break;
      }
  }
  
  return answer;  // 정답 반환
}