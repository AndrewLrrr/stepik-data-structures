class Node:
    def __init__(self, left=None, right=None, value=None, size=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = size if size is not None else len(value)
        self.height = 1

    def __repr__(self):
        return str({'size': self.size, 'height': self.height, 'value': self.value})


class Rope:
    MAX_STRING_LENGTH = 32

    @staticmethod
    def balance(node):
        if node is None:
            return None
        Rope.update(node)
        balance_factor = Rope.balance_factor(node)
        while balance_factor < -1 or balance_factor > 1:
            if balance_factor > 1:
                if Rope.balance_factor(node.right) < 0:
                    node.right = Rope.rotate_right(node.right)
                node = Rope.rotate_left(node)
            elif balance_factor < -1:
                if Rope.balance_factor(node.left) > 0:
                    node.left = Rope.rotate_left(node.left)
                node = Rope.rotate_right(node)
            balance_factor = Rope.balance_factor(node)
        return node

    @staticmethod
    def find(key, node):
        if node.left is not None:
            if Rope.size(node.left) < key:
                return Rope.find(key - node.left.size, node.right)
            else:
                return Rope.find(key, node.left)
        else:
            return node.value[key]

    @staticmethod
    def add(value, node=None):
        if node is None:
            return Node(value=value)
        node.right = Rope.add(value, node.right)
        return Rope.balance(node)

    @staticmethod
    def rotate_right(node):
        top_node = node.left
        if top_node:
            node.left = top_node.right
            top_node.right = node
            Rope.update(node)
            Rope.update(top_node)
            return top_node
        return node

    @staticmethod
    def rotate_left(node):
        top_node = node.right
        if top_node:
            node.right = top_node.left
            top_node.left = node
            Rope.update(node)
            Rope.update(top_node)
            return top_node
        return node

    @staticmethod
    def balance_factor(node):
        if node is None:
            return 0
        return Rope.height(node.right) - Rope.height(node.left)

    @staticmethod
    def update(node):
        Rope.update_height(node)
        Rope.update_size(node)

    @staticmethod
    def update_height(node):
        h_l = Rope.height(node.left)
        h_r = Rope.height(node.right)
        node.height = (h_l if h_l > h_r else h_r) + 1

    @staticmethod
    def update_size(node):
        node.size = Rope.size(node.left) + Rope.size(node.right)

    @staticmethod
    def height(node):
        return node.height if node else 0

    @staticmethod
    def size(node):
        return node.size if node else 0

    @staticmethod
    def merge(node1, node2):
        if node1 is None:
            return node2
        elif node2 is None:
            return node1
        else:
            size = Rope.size(node1) + Rope.size(node2)
            if size <= Rope.MAX_STRING_LENGTH:
                return Node(value=(Rope.to_string(node1) + Rope.to_string(node2)))
            return Rope.balance(Node(left=node1, right=node2, size=size))

    @staticmethod
    def split(key, node):
        if node.left is not None:
            if Rope.size(node.left) >= key:
                first, second = Rope.split(key, node.left)
                tree1 = first
                tree2 = Rope.merge(second, node.right)
            else:
                first, second = Rope.split(key - Rope.size(node.left), node.right)
                tree1 = Rope.merge(node.left, first)
                tree2 = second
        else:
            prefix = node.value[0:key]
            postfix = node.value[key:]
            tree1 = Node(value=prefix) if prefix else None
            tree2 = Node(value=postfix) if postfix else None
        return tree1, tree2

    @staticmethod
    def reorder(start, finish, position, node):
        if start < 0:
            start = 0
        if finish >= node.size:
            return node
        if start == 0:
            sub_str, string = Rope.split(finish - start + 1, node)
        else:
            prefix, sub_str = Rope.split(start, node)
            sub_str, postfix = Rope.split(finish - start + 1, sub_str)
            string = Rope.merge(prefix, postfix)
        rope = Rope.insert(position, string, sub_str)
        return rope

    @staticmethod
    def insert(key, node, inserted):
        if key == 0:
            return Rope.merge(inserted, node)
        elif key >= node.size:
            return Rope.merge(node, inserted)
        prefix, postfix = Rope.split(key, node)
        return Rope.merge(Rope.merge(prefix, inserted), postfix)

    @staticmethod
    def to_string(node):
        def crawler(node, string=''):
            if node is not None:
                string = crawler(node.left, string)
                if node.value is not None:
                    string += node.value
                string = crawler(node.right, string)
            return string
        return crawler(node)

    @staticmethod
    def debug(node):
        def crawler(node, nodes):
            if node is not None:
                nodes = crawler(node.left, nodes)
                nodes.append(node)
                nodes = crawler(node.right, nodes)
            return nodes
        return crawler(node, [])


def main():
    rope = Rope.add(input())
    total = int(input())
    for i in range(total):
        start, finish, position = [int(i) for i in input().split()]
        rope = Rope.reorder(start, finish, position, rope)
    print(Rope.to_string(rope))


if __name__ == '__main__':
    main()
