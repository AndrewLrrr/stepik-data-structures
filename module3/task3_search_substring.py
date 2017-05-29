def custom_hash(string):
    return sum(ord(l) for l in list(string))


def search_substring(string, sub_string):
    matches = []

    str_length = len(string)
    sub_str_length = len(sub_string)

    base_hash = custom_hash(string[:sub_str_length:])
    sub_str_hash = custom_hash(sub_string)

    for i in range(0, str_length - sub_str_length + 1):
        next_idx = sub_str_length + i
        prev = 0 if i == 0 else ord(string[i - 1])
        last = 0 if i == 0 else ord(string[next_idx - 1])
        base_hash = base_hash - prev + last
        if base_hash == sub_str_hash and sub_string == string[i:next_idx]:
            matches.append(i)

    return matches


def main():
    sub_string = input()
    string = input()
    print(*search_substring(string, sub_string))


if __name__ == '__main__':
    main()


# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string = ''.join(random.choice(letters + letters.lower()) for _ in range(10000000))
# sub_string = ''.join(random.choice(letters + letters.lower()) for _ in range(10))
#
# print(sub_string)
#
# start_time = time.time()
# print(*search_substring(string, sub_string))
# print("--- %s seconds ---" % (time.time() - start_time))

