class HashMap:
    def __init__(self, size: int):
        self.size = size
        self._hash_lst = [None for i in range(self.size)]

    def hash_code(self, key: int):
        return key % self.size

    def add(self, key):
        self._hash_lst[self.hash_code(key)] = key

    def remove(self, key):
        self._hash_lst[self.hash_code(key)] = None

    def get(self, key):
        index = self.hash_code(key)
        if index <= len(self._hash_lst):
            if self._hash_lst[index] is not None:
                return self._hash_lst[index]
        return -1


def main():
    hm = HashMap(64)
    hm.add(203)
    hm.add(50)
    hm.add(60)
    print(hm.get(50))


if __name__ == "__main__":
    main()