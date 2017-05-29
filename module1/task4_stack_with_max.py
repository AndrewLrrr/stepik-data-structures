class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__stack_max = []

    def push(self, value):
        self.__stack.append(value)
        current_max = self.__stack_max[-1] if self.__stack_max else value
        if current_max < value:
            self.__stack_max.append(value)
        else:
            self.__stack_max.append(current_max)
        return True

    def pop(self):
        if not self.__stack:
            raise Exception('Stack is empty')
        self.__stack_max.pop()
        return self.__stack.pop()

    def max(self):
        if not self.__stack:
            raise Exception('Stack is empty')
        return self.__stack_max[-1]


def main():
    count = int(input())
    stack = StackWithMax()
    for i in range(count):
        inp = input().split()
        if inp[0] == 'push':
            stack.push(int(inp[1]))
        elif inp[0] == 'pop':
            stack.pop()
        else:
            print(stack.max())


if __name__ == '__main__':
    main()
