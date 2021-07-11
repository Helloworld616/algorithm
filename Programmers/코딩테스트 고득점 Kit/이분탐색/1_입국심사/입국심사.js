// 이분 탐색 함수
function binarySearch(min_time, max_time, times, compare, n) {
    let mid_time = parseInt((min_time + max_time)/2);  // 중간값
    
    // 최대 시간이 최소 시간보다 작아질 경우 더 이상 탐색이 불가하므로 compare 반환
    if (max_time < min_time) {
        return compare;
    }
    
    // 현재 중간값이 수용할 수 있는 인원 수 total 구하기
    let total = 0;
    times.forEach(el => {
        total += parseInt(mid_time / el);  
    });
    
    // 1. total이 n 이상이면 중간값과 비교값을 비교하여, 비교값을 더 작은 값으로 갱신. 이후 다음 탐색 실시
    // 2. total이 n보다 작을 경우, 수용 불가 상태라 중간값이 아예 답이 될 수 없으므로 바로 다음 탐색 실시 
    if (total >= n) {
        if (mid_time < compare) {
            compare = mid_time;
        }
        return binarySearch(min_time, mid_time - 1, times, compare, n);
    } else {
        return binarySearch(mid_time + 1, max_time, times, compare, n);
    }
}


// 답안 함수
function solution(n, times) {
    // 입력 받은 배열 times를 오름차순으로 정렬
    times.sort(function(a, b) {
        return a - b;
    })
    
    let min_time = times[0];  // 최소 시간
    let max_time = times[times.length - 1] * n;  // 최대 시간
    let compare = max_time;  // 이분 탐색 시 중간값과 비교할 값 -> 이 값이 곧 정답이 된다!

    // 이분 탐색을 통해 정답 구하기
    const answer = binarySearch(min_time, max_time, times, compare, n);
    
    // 정답 반환
    return answer;
}