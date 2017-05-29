import sys

sys.setrecursionlimit(50000)


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

    def is_empty(self):
        return len(self.nodes) == 0

    def add(self, value, l_key, r_key):
        self.nodes.append(Node(self, value, l_key, r_key))


class TreePropertiesChecker:
    def __init__(self, tree):
        self.tree = tree

    def _crawler(self, node):
        if node is not None:
            left_value = self._crawler(node.left)
            right_value = self._crawler(node.right)
            if left_value is None and right_value is None:
                return [node.value, node.value]
            if left_value is None:
                r_min, r_max = right_value
                if node.value > r_min:
                    raise Exception('INCORRECT')
                return [min(r_min, node.value), max(r_max, node.value)]
            if right_value is None:
                l_min, l_max = left_value
                if node.value <= l_max:
                    raise Exception('INCORRECT')
                return [min(l_min, node.value), max(l_max, node.value)]
            r_min, r_max = right_value
            l_min, l_max = left_value
            if node.value > r_min or node.value <= l_max:
                raise Exception('INCORRECT')
            return [min(r_min, l_min, node.value), max(r_max, l_max, node.value)]

    def run(self):
        if self.tree.is_empty():
            return 'CORRECT'

        try:
            self._crawler(self.tree.get_root())
        except Exception as e:
            return str(e)
        return 'CORRECT'


def main():
    total = int(input())
    tree = Tree()
    for i in range(total):
        tree.add(*[int(i) for i in input().split()])
    tree_checker = TreePropertiesChecker(tree)
    print(tree_checker.run())


if __name__ == '__main__':
    main()
