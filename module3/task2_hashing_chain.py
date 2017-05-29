class HashTable:
    def __init__(self, length):
        self._storage = {}
        self._length = length

    def _hash(self, string):
        p = 1000000007
        x = 263
        h = 0
        for idx, char in enumerate(list(string)):
            char_code = ord(char)
            h = (h + (char_code * ((x ** idx) % p))) % p
        return h % self._length

    def add(self, string):
        h = self._hash(string)
        if h in self._storage:
            if string not in self._storage[h]:
                self._storage[h] = [string] + self._storage[h]
        else:
            self._storage[h] = [string]

    def find(self, string):
        h = self._hash(string)
        return 'yes' if h in self._storage and string in self._storage[h] else 'no'

    def delete(self, string):
        h = self._hash(string)
        if h in self._storage and string in self._storage[h]:
            if len(self._storage[h]) == 1:
                del self._storage[h]
            else:
                self._storage[h].remove(string)

    def check(self, index):
        return ' '.join(self._storage[index]) if index in self._storage else ''


def main():
    length = int(input())
    total = int(input())
    ht = HashTable(length)
    for i in range(total):
        action, value = input().split()
        if action == 'add':
            ht.add(value)
        elif action == 'find':
            print(ht.find(value))
        elif action == 'del':
            ht.delete(value)
        elif action == 'check':
            print(ht.check(int(value)))


if __name__ == '__main__':
    main()
