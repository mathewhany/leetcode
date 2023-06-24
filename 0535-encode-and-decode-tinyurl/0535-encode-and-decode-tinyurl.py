class Codec:
    alphabet = '0123456789' + string.ascii_letters

    def __init__(self):
        self.decodeMap = {}
        self.baseUrl = "http://tinyurl.com/"
        self.nextId = 0

    def encode(self, longUrl: str) -> str:
        base = len(self.alphabet)
        encoded = ''
        currentId = self.nextId
        self.nextId += 1
        while currentId > 0:
            encoded = alphabet[current % base] + encoded
            currentId = currentId // base
        shortUrl = self.baseUrl + (encoded if len(encoded) > 0 else '0')
        self.decodeMap[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))