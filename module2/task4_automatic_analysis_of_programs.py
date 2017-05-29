class VariablesAnalyzer:
    def __init__(self, count):
        self.__parent = {}
        self.__rank = {}
        for i in range(1, count + 1):
            self.make_set(i)

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
            return False
        if self.__rank[i_id] > self.__rank[j_id]:
            self.__parent[j_id] = i_id
        else:
            self.__parent[i_id] = j_id
            if self.__rank[i_id] == self.__rank[j_id]:
                self.__rank[j_id] += 1
        return True

    def add_equality(self, i, j):
        return self.union(i, j)

    def add_inequality(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        return self.__parent[i_id] != self.__parent[j_id]


def main():
    has_conflict = False
    variables_count, equals_count, inequals_count = [int(i) for i in input().split()]
    va = VariablesAnalyzer(variables_count)
    for i in range(equals_count):
        va.add_equality(*[int(i) for i in input().split()])
    for j in range(inequals_count):
        if va.add_inequality(*[int(i) for i in input().split()]) is False:
            has_conflict = True
            break
    print(0 if has_conflict else 1)


if __name__ == '__main__':
    main()
