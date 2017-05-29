class MinHeap:
    def __init__(self, elements):
        self.__log = []
        self.__heap = elements
        self.__size = len(elements)
        self.__build()

    @staticmethod
    def __parent(i) -> int:
        return (i - 1) // 2

    @staticmethod
    def __left_child(i) -> int:
        return 2 * i + 1

    @staticmethod
    def __right_child(i) -> int:
        return 2 * i + 2

    def __shift_up(self, i):
        while i > 0 and self.__heap[self.__parent(i)] > self.__heap[i]:
            self.__heap[self.__parent(i)], self.__heap[i] = self.__heap[i], self.__heap[self.__parent(i)]
            self.__log.append((i, self.__parent(i)))
            i = self.__parent(i)

    def __shift_down(self, i):
        while self.__left_child(i) < self.__size:
            left = self.__left_child(i)
            right = self.__right_child(i)
            min_index = left
            if right < self.__size and self.__heap[right] < self.__heap[min_index]:
                min_index = right
            if self.__heap[i] <= self.__heap[min_index]:
                break
            self.__heap[i], self.__heap[min_index] = self.__heap[min_index], self.__heap[i]
            self.__log.append((i, min_index))
            i = min_index

    def __build(self):
        base = self.__size // 2
        for i in range(base, -1, -1):
            self.__shift_down(i)

    def insert(self, key):
        self.__size += 1
        self.__heap[self.__size - 1] = key
        self.__shift_up(self.__size - 1)

    def extract_min(self):
        top = self.__heap[0]
        self.__size -= 1
        self.__heap[0] = self.__heap[self.__size]
        self.__shift_down(0)
        return top

    def log(self):
        return self.__log


def main():
    elements_len = int(input())
    min_heap = MinHeap([int(i) for i in input().split()])
    build_log = min_heap.log()
    print(len(build_log))
    for item in build_log:
        print(*item)

if __name__ == '__main__':
    main()
