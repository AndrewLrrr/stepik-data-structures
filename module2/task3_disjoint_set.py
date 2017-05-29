class DatabaseEmulator:
    def __init__(self, tables):
        self.__max = max(tables)
        self.__tables = dict(zip(range(1, len(tables) + 1), tables))
        self.__set = DisjointSet()
        for key, item in self.__tables.items():
            self.__set.make_set(key)

    def max(self):
        return self.__max

    def join(self, destination, source):
        parent, source = self.__set.union(source, destination)
        if parent != source:
            self.__tables[parent] += self.__tables[source]
        if self.__tables[parent] > self.__max:
            self.__max = self.__tables[parent]


class DisjointSet:
    def __init__(self):
        self.__parent = {}
        self.__rank = {}

    def make_set(self, i):
        self.__parent[i] = i
        self.__rank[i] = 0

    def find(self, i):
        while i != self.__parent[i]:
            i = self.__parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return j_id, j_id
        if self.__rank[i_id] > self.__rank[j_id]:
            self.__parent[j_id] = i_id
            return i_id, j_id
        else:
            self.__parent[i_id] = j_id
            if self.__rank[i_id] == self.__rank[j_id]:
                self.__rank[j_id] += 1
            return j_id, i_id


def main():
    total_tables, total_joins = [int(i) for i in input().split()]
    tables = [int(i) for i in input().split()]
    db = DatabaseEmulator(tables)
    for join in range(total_joins):
        db.join(*[int(i) for i in input().split()])
        print(db.max())


if __name__ == '__main__':
    main()
