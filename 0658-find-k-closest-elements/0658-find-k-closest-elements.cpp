class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int start = 0;
        int end = k - 1;
        
        for (int i = k; i < arr.size(); i++) {
            if (closer(arr[i - k], arr[i], x)) break;

            start++;
            end++;
        }

        vector<int> ans;
        for (int i = start; i <= end; i++) ans.push_back(arr[i]);

        return ans;
    }
private:
    bool closer(int a, int b, int x) {
        return (abs(a - x) < abs(b - x) || abs(a - x) == abs(b - x) && a < b);
    }
};