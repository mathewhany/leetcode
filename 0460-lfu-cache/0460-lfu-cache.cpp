class LFUCache {
    unordered_map<int, int> key_to_freq;
    unordered_map<int, list<int>::iterator> key_to_node;
    unordered_map<int, int> key_to_val;
    unordered_map<int, list<int>> freq_to_list;
    int size = 0;
    int minFreq = 1;
    int capacity;
    
public:
    LFUCache(int capacity) : capacity(capacity)  {
    }
    
    int get(int key) {
        if (key_to_val.count(key)) {
            int val = key_to_val[key];
            updateFreq(key);
            return val;
        }

        return -1;
    }
    
    void put(int key, int value) {
        key_to_val[key] = value;

        if (key_to_freq.count(key)) {
            updateFreq(key);
        } else {
            if (size >= capacity) {
                int minKey = freq_to_list[minFreq].front();
                freq_to_list[minFreq].pop_front();
                key_to_val.erase(minKey);
                key_to_node.erase(minKey);
                key_to_freq.erase(minKey);
            }
            freq_to_list[1].push_back(key);
            key_to_freq[key] = 1;
            key_to_node[key] = --freq_to_list[1].end();
            minFreq = min(minFreq, 1);
            size++;
        }
    }

private:
    void updateFreq(int key) {
        int freq = key_to_freq[key];
        list<int>::iterator node = key_to_node[key];

        freq_to_list[freq].erase(node);
        freq_to_list[freq + 1].push_back(key);
        key_to_freq[key]++;
        key_to_node[key] = --freq_to_list[freq + 1].end();

        if (freq == minFreq && freq_to_list[freq].empty()) {
            minFreq++;
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */