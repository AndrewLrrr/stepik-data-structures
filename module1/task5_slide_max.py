class SlideMaxList:
    def __init__(self, size, values):
        self.__queue = []
        self.__max_deque = []
        self.__buffer = []
        self.__size = size
        self.__values = values

    def __iter__(self):
        for value in self.__values:
            if len(self.__queue) >= self.__size:
                extra_value = self.__queue.pop(0)
                self.__update_max(extra_value)
            self.__queue.append(value)
            self.__add_max(value)
        return iter(self.__buffer)

    def __update_max(self, value):
        if self.__max_deque:
            if self.__max_deque[0] == value:
                self.__max_deque.pop(0)

    def __add_max(self, value):
        if self.__max_deque:
            current_max = self.__max_deque[0]
            if current_max < value:
                self.__max_deque[0] = value
            else:
                while self.__max_deque[-1] < value:
                    self.__max_deque.pop()
                self.__max_deque.append(value)
        else:
            self.__max_deque.append(value)
        if len(self.__queue) >= self.__size:
            self.__buffer.append(self.__max_deque[0])


def main():
    total = int(input())
    values = [int(i) for i in input().split()]
    size = int(input())
    print(*SlideMaxList(size, values))


if __name__ == '__main__':
    main()
