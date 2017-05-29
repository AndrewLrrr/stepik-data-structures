def tree_height_decoder(code):
    tree_map = {}
    root = 0
    height = 1

    if len(code) == 1:
        return 1

    for idx, item in enumerate(code):
        if item == -1:
            root = idx
        else:
            if item not in tree_map:
                tree_map[item] = [idx]
            else:
                tree_map[item].append(idx)

    roots = tree_map[root]

    while roots:
        height += 1
        tmp_roots = roots
        roots = []
        for root in tmp_roots:
            if root in tree_map:
                roots += tree_map[root]

    return height


if __name__ == '__main__':
    total = int(input())
    encoded_tree = [int(i) for i in input().split()]
    print(tree_height_decoder(encoded_tree))


# def get_root(code):
#     for idx, item in enumerate(code):
#         if item == -1:
#             return idx


# def tree_height_decoder(code):
#     def get_height(root, level):
#         height = level
#         if root not in code:
#             return level
#         for idx, item in enumerate(code):
#             if item == root:
#                 height = max(height, get_height(idx, level + 1))
#         return height
#     return get_height(get_root(code), 1)
#

# def tree_height_decoder(code):
#     roots = [get_root(code)]
#     height = 0
#     while roots:
#         height += 1
#         tmp_roots = roots
#         roots = []
#         for root in tmp_roots:
#             if root in code:
#                 for idx, item in enumerate(code):
#                     if item == root:
#                         roots.append(idx)
#     return height
