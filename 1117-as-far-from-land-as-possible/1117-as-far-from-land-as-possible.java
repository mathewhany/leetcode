class Solution {
    private final int[][] directions = new int[][] {
        new int[] { 1, 0 },
        new int[] { -1, 0 },
        new int[] { 0, 1 },
        new int[] { 0, -1 }
    };

    public int maxDistance(int[][] grid) {
        int n = grid.length;
        int[][] distances = new int[n][n];
        boolean[][] visited = new boolean[n][n];
        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        int dist = 0;
        int ans = -1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                distances[i][j] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    queue.offer(new Pair(i, j));
                }
            }
        }
        
        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            for (int k = 0; k < queueSize; k++) {
                Pair<Integer, Integer> pair = queue.poll();
                int pairI = pair.getKey();
                int pairJ = pair.getValue();

                distances[pairI][pairJ] = Math.min(distances[pairI][pairJ], dist);

                for (int d = 0; d < directions.length; d++) {
                    int[] direction = directions[d];
                    int di = direction[0];
                    int dj = direction[1];

                    int ii = pairI + di;
                    int jj = pairJ + dj;

                    if (ii >= 0 && ii < n && jj >= 0 && jj < n && !visited[ii][jj]) {
                        visited[ii][jj] = true;
                        queue.offer(new Pair(ii, jj));
                    } 
                }
            }

            dist++;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans = Math.max(ans, distances[i][j]);
            }
        }

        return ans == Integer.MAX_VALUE || ans == 0 ? -1 : ans;
    }
}