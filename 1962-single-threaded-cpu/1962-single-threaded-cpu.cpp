class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        for (int i = 0; i < n; i++) tasks[i].push_back(i);

        sort(tasks.begin(), tasks.end());

        int currentTask = 0;
        long long time = 0;
        vector<int> ans;

        while (currentTask < n || !pq.empty()) {
            while (currentTask < n && tasks[currentTask][0] <= time) {
                pq.push(make_pair(tasks[currentTask][1], tasks[currentTask][2]));
                currentTask++;
            }

            if (pq.empty()) {
                time = tasks[currentTask][0];
            } else {
                auto [procTime, taskIndex] = pq.top();
                time += procTime;
                ans.push_back(taskIndex);
                pq.pop();
            }
        }

        return ans;
    }
};