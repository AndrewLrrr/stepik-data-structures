class Node:
    def __init__(self, tree, value, l_key, r_key):
        self.tree = tree
        self.l_key = l_key
        self.r_key = r_key
        self.value = value

    def __getattr__(self, name):
        if name == 'left':
            return self.tree.nodes[self.l_key] if self.l_key > -1 else None
        elif name == 'right':
            return self.tree.nodes[self.r_key] if self.r_key > -1 else None


class Tree:
    def __init__(self):
        self.nodes = []

    def get_root(self):
        return self.nodes[0]

    def add(self, value, l_key, r_key):
        self.nodes.append(Node(self, value, l_key, r_key))


class TreeCrawler:
    def __init__(self, tree):
        self.tree = tree
        self.ordered_list = []

    def in_order(self):
        self.ordered_list = []

        def crawler(node):
            if node is not None:
                crawler(node.left)
                self.ordered_list.append(node.value)
                crawler(node.right)
        crawler(self.tree.get_root())
        return self.ordered_list

    def pre_order(self):
        self.ordered_list = []

        def crawler(node):
            if node is not None:
                self.ordered_list.append(node.value)
                crawler(node.left)
                crawler(node.right)
        crawler(self.tree.get_root())
        return self.ordered_list

    def post_order(self):
        self.ordered_list = []

        def crawler(node):
            if node is not None:
                crawler(node.left)
                crawler(node.right)
                self.ordered_list.append(node.value)
        crawler(self.tree.get_root())
        return self.ordered_list


def main():
    total = int(input())
    tree = Tree()
    for i in range(total):
        tree.add(*[int(i) for i in input().split()])
    tree_crawler = TreeCrawler(tree)
    print(*tree_crawler.in_order())
    print(*tree_crawler.pre_order())
    print(*tree_crawler.post_order())


if __name__ == '__main__':
    main()
