class SummaryRanges {
    set<int> nums;
public:
    SummaryRanges() {
        
    }
    
    void addNum(int value) {
        nums.insert(value);
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> ans;
        int start = -1, end = -1;
        bool isFirst = true;

        for (const auto &num : nums) {
            if (isFirst) {
                start = end = num;
                isFirst = false;
                continue;
            }

            if (end + 1 == num) {
                end = num;
                continue;
            }

            vector<int> interval;
            interval.push_back(start);
            interval.push_back(end);
            ans.push_back(interval);

            start = end = num;
        }

        if (!isFirst) {
            vector<int> interval;
            interval.push_back(start);
            interval.push_back(end);
            ans.push_back(interval);
        }

        return ans;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */