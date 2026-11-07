class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        total = 0
        for char in string:
            total += ord(char)
        return total

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]

    def lookup(self, key):
        hash_key = self.hash(key)
        return self.collection.get(hash_key, {}).get(key)
