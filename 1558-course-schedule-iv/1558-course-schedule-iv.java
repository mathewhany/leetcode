class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        int n = numCourses;
        int p = prerequisites.length;
        boolean[][] matrix = new boolean[n][n];

        for (int[] prerequisite : prerequisites) {
            int from = prerequisite[0];
            int to = prerequisite[1];

            matrix[from][to] = true;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = matrix[i][j] || matrix[i][k] && matrix[k][j];
                }
            }
        }

        List<Boolean> ans = new ArrayList<>();

        for (int[] query : queries) {
            int from = query[0];
            int to = query[1];

            ans.add(matrix[from][to]);
        }

        return ans;
    }
}