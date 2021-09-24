import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
        /* 이차원 배열을 순회하여 값 계산 */
        for (int i = 1; i < triangle.length; i++) {
            for (int j = 0; j < triangle[i].length; j ++) {
                /* 1. 첫 원소면 이전 배열의 같은 인덱스 원소를 더함. */
                if (j == 0) {
                    triangle[i][j] += triangle[i-1][j]; 
                }
                /* 2. 마지막 원소면 이전 배열의 (현재 인덱스 - 1) 원소를 더함. */
                else if (j == triangle[i].length - 1) {
                    triangle[i][j] += triangle[i-1][j-1]; 
                }
                /* 3. 그 이외의 원소면 이전 배열의 대각선 원소 중 더 큰 것을 더함. */ 
                else {
                    triangle[i][j] += Math.max(triangle[i-1][j-1], triangle[i-1][j]); 
                }
            } 
        }
        
        /* 이차원 배열의 마지막 원소 정렬 */
        Arrays.sort(triangle[triangle.length-1]); 
        
        /* 이차원 배열의 마지막 원소의 마지막 값을 정답에 할당 */
        int answer = triangle[triangle.length-1][triangle[triangle.length-1].length-1]; 
        
        return answer; // 정답 반환
    }
}