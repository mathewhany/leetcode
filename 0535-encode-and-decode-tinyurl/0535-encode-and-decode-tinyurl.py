class Codec:

    def __init__(self):
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"
        self.current = 0

    def encode(self, longUrl: str) -> str:
        url = self.base + str(self.current)
        self.current += 1
        self.decodeMap[url] = longUrl
        return url

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))