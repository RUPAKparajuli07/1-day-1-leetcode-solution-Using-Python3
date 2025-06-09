import random
import string

class Codec:
    def __init__(self):
        self.url_map = {}         # short -> long
        self.reverse_map = {}     # long -> short
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        # If already encoded
        if longUrl in self.reverse_map:
            return self.base_url + self.reverse_map[longUrl]

        # Generate a unique short key
        while True:
            key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            if key not in self.url_map:
                break

        self.url_map[key] = longUrl
        self.reverse_map[longUrl] = key
        return self.base_url + key

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.replace(self.base_url, '')
        return self.url_map.get(key, "")
