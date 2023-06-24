class Codec:
    alphabet = '0123456789' + string.ascii_letters

    def __init__(self):
        self.decodeMap = {}
        self.baseUrl = "http://tinyurl.com/"
        self.nextId = 0

    def encode(self, longUrl: str) -> str:
        while True:
            shortUrl = self.baseUrl + ''.join(random.choice(self.alphabet) for _ in range(10))
            if shortUrl not in self.decodeMap:
                self.decodeMap[shortUrl] = longUrl
                return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))