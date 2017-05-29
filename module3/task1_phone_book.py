class PhoneBook:
    def __init__(self):
        self.__storage = {}

    def add(self, number, name):
        self.__storage[number] = name

    def find(self, number):
        if number in self.__storage:
            return self.__storage[number]
        return 'not found'

    def delete(self, number):
        if number in self.__storage:
            del self.__storage[number]


def main():
    total = int(input())
    pb = PhoneBook()
    for i in range(total):
        query = input().split()
        if query[0] == 'add':
            pb.add(query[1], query[2])
        elif query[0] == 'find':
            print(pb.find(query[1]))
        elif query[0] == 'del':
            pb.delete(query[1])


if __name__ == '__main__':
    main()

