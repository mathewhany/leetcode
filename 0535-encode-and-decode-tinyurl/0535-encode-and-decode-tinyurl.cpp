class Solution {
private:
    unordered_map<string, string> shortToLong;
    int nextShort = 0;
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        string short_url = "http://tinyurl.com/" + to_string(nextShort++);
        shortToLong[short_url] = longUrl;
        return short_url;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return shortToLong[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));