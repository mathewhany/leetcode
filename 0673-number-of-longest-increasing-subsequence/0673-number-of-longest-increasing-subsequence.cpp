class MaxElement {
public:
        MaxElement() : maxElement(0), maxElementCnt(1) {}

        void add(int element, int count) {
            if (element > maxElement) {
                maxElement = element;
                maxElementCnt = count;
            } else if (element == maxElement) {
                maxElementCnt += count;
            }
        }

        int getMax() {
            return maxElement;
        }

        int getCount() { 
            return maxElementCnt; 
        }
private:
        int maxElement;
        int maxElementCnt;
};

class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> length(n, 0), cnt(n, 0);

        for (int i = 0; i < n; i++) {
            MaxElement me;

            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    me.add(length[j], cnt[j]);
                }
            }

            length[i] = me.getMax() + 1;
            cnt[i] = me.getCount();
        }

        MaxElement me;
        for (int i = 0; i < n; i++) {
            me.add(length[i], cnt[i]);
        }
        
        return me.getCount();
    }
};