/* 배열의 원소를 문자로 바꾸는 함수 */
function numToString(array) {
  array.forEach((el, idx) => {
      const stringEl = String(el) // 원소를 문자열로 변경
      const dotIdx = stringEl.indexOf('.') // 원소가 소수일 경우, 소수점의 위치를 계산
      let integer = '' // 소수의 정수부를 담을 변수 초기화
      
      /* 소수의 정수부를 구한다 */
      if (dotIdx !== -1) {
          integer = stringEl.slice(0, dotIdx)
      }
      
      /* 1. 문자열로 변환한 원소의 길이, 혹은 소수의 정수부의 길이가 1일 경우, 앞에 0을 붙이고 원소를 교체한다. (자릿수를 맞추기 위함!) */
      /* 2. 아닐 경우 바로 변환한 문자열로 원소를 교체한다. */
      if (stringEl.length === 1 || integer.length === 1) {
          array[idx] = '0' + stringEl
      } else {
          array[idx] = stringEl
      }
  })
}


/* 최대 요청 개수를 찾는 함수 */
function findMax(array) {
  let ans = 0 // 반환할 정답 초기화
  
  array.forEach(x => {
      /* 1. 시작 시각 근방의 요청 개수 세기 */
      let cnt = 0
      array.forEach(y => {
          if ((x[0] <= y[1] && y[0] < x[0] + 1)) {
              cnt++
          }
      })
      if (ans < cnt) {
          ans = cnt
      }
      
      /* 2. 종료 시각 근방의 요청 개수 세기 */
      cnt = 0
      array.forEach(y => {
          if ((x[1] <= y[1] && y[0] < x[1] + 1)) {
              cnt++
          }
      })
      if (ans < cnt) {
          ans = cnt
      }
  })
  
  return ans // 정답 반환
}


/* 솔루션 함수 */
function solution(lines) {
  let processor = [] // 시간을 기록할 배열 생성
  
  /* lines 안의 정보들을 이용해 로그의 시작 시각과 종료 시각을 계산 */
  lines.forEach(line => {
      const list = line.split(' ') // 공백을 기준으로 정보를 분리하여 배열 생성
      
      /* 종료 날짜와 종료 시각을 계산 */
      const endDay = list[0].split('-').map(x => parseFloat(x))
      const endTime = list[1].split(':').map(x => parseFloat(x))
      
      /* 시작 날짜와 시작 시각을 초기화 */
      const startDay = list[0].split('-').map(x => parseFloat(x))
      const startTime = list[1].split(':').map(x => parseFloat(x))
      
      /* 처리 시간을 실수로 변경 */
      const second = parseFloat(list[2].substr(0, list[2].length - 1)) - 0.001
      
      /* 종료 시각에서 처리 시간을 빼서 시작 시각을 구한다 */
      if (startTime[2] < second) {
          startTime[2] += 60
          
          if (startTime[1] === 0) {
              startTime[1] = 59
              
              if (endTime[0] === 0) {
                  startTime[0] = 23
                  startDay[2] -= 1
              } else {
                  startTime[0] -= 1
              }
          } else {
              startTime[1] -= 1
          }
      }
      startTime[2] -= second
      startTime[2] = startTime[2].toFixed(3)
      
      /* 배열의 원소들을 문자열로 변경 */
      numToString(startDay)
      numToString(startTime)
      numToString(endDay)
      numToString(endTime)
      
      /* 배열 안의 원소들을 하나의 문자열로 합친 뒤 실수로 변환 */
      const start = parseFloat(startDay.join('') + startTime.join(''))
      const end = parseFloat(endDay.join('') + endTime.join(''))

      /* 최종적으로 산출된 시작 시각과 끝 시각을 배열 processor에 추가 */
      processor.push([start, end])
  })
  
  const answer = findMax(processor) // 최대 요청 개수 구하기
  
  return answer; // 정답 반환
}