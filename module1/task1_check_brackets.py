def check_brackets(string):
    string = list(string)
    open_brackets_stack = []
    open_brackets_idx_stack = []
    counter = 0

    for item in string:
        counter += 1
        if item not in ['(', '[', '{', '}', ']', ')']:
            continue
        if item in ['(', '[', '{']:
            open_brackets_idx_stack.append(counter)
            open_brackets_stack.append(item)
        elif not open_brackets_stack:
            return counter
        else:
            last = open_brackets_stack.pop()
            open_brackets_idx_stack.pop()
            if (last == '(' and item != ')') \
                    or (last == '[' and item != ']') \
                    or (last == '{' and item != '}') \
                    or not last:
                return counter

    if not open_brackets_stack:
        return -1
    else:
        while len(open_brackets_idx_stack) > 1:
            open_brackets_idx_stack.pop()
        return open_brackets_idx_stack.pop()


if __name__ == '__main__':
    res = check_brackets(input())
    if res < 0:
        print('Success')
    else:
        print(res)
