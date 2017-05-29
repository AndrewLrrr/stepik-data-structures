class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.sum = key

    def __repr__(self):
        return str({'key': self.key, 'height': self.height, 'sum': self.sum})


class AVLTree:
    @staticmethod
    def balance(node):
        if node is None:
            return None
        AVLTree.update(node)
        if AVLTree.balance_factor(node) > 1:
            if AVLTree.balance_factor(node.right) < 0:
                node.right = AVLTree.rotate_right(node.right)
            node = AVLTree.rotate_left(node)
        if AVLTree.balance_factor(node) < -1:
            if AVLTree.balance_factor(node.left) > 0:
                node.left = AVLTree.rotate_left(node.left)
            node = AVLTree.rotate_right(node)
        return node if -1 <= AVLTree.balance_factor(node) <= 1 else AVLTree.balance(node)

    @staticmethod
    def max(node):
        if node is None:
            return Node(float('inf'))
        else:
            if node.right is None:
                return node
            return AVLTree.max(node.right)

    @staticmethod
    def min(node):
        if node is None:
            return Node(-float('inf'))
        else:
            if node.left is None:
                return node
            return AVLTree.min(node.left)

    @staticmethod
    def find(key, node):
        if node is None:
            return None
        else:
            if node.key == key:
                return node
            elif node.key > key:
                return AVLTree.find(key, node.left)
            elif node.key < key:
                return AVLTree.find(key, node.right)

    @staticmethod
    def add(key, node):
        if node is None:
            return Node(key)
        if node.key > key:
            node.left = AVLTree.add(key, node.left)
        elif node.key < key:
            node.right = AVLTree.add(key, node.right)
        return AVLTree.balance(node)

    @staticmethod
    def rotate_right(node):
        top_node = node.left
        if top_node:
            node.left = top_node.right
            top_node.right = node
            AVLTree.update(node)
            AVLTree.update(top_node)
            return top_node
        return node

    @staticmethod
    def rotate_left(node):
        top_node = node.right
        if top_node:
            node.right = top_node.left
            top_node.left = node
            AVLTree.update(node)
            AVLTree.update(top_node)
            return top_node
        return node

    @staticmethod
    def balance_factor(node):
        if node is None:
            return 0
        return AVLTree.height(node.right) - AVLTree.height(node.left)

    @staticmethod
    def update(node):
        AVLTree.update_height(node)
        AVLTree.update_sum(node)

    @staticmethod
    def update_height(node):
        node.height = max(AVLTree.height(node.left), AVLTree.height(node.right)) + 1

    @staticmethod
    def update_sum(node):
        node.sum = AVLTree.sum(node.left) + AVLTree.sum(node.right) + node.key

    @staticmethod
    def remove(key, node):
        if node is None:
            return None
        if node.key > key:
            node.left = AVLTree.remove(key, node.left)
        elif node.key < key:
            node.right = AVLTree.remove(key, node.right)
        else:
            l_node = node.left
            r_node = node.right
            del node
            if r_node is None:
                return l_node
            _min = AVLTree.find_min(r_node)
            _min.right = AVLTree.remove_min(r_node)
            _min.left = l_node
            return AVLTree.balance(_min)
        return AVLTree.balance(node)

    @staticmethod
    def remove_min(node):
        if node.left is None:
            return node.right
        node.left = AVLTree.remove_min(node.left)
        return AVLTree.balance(node)

    @staticmethod
    def find_min(node):
        return AVLTree.find_min(node.left) if node.left else node

    @staticmethod
    def height(node):
        return node.height if node else 0

    @staticmethod
    def sum(node):
        return node.sum if node else 0


class IntervalSet:
    def __init__(self):
        self.s = 0
        self.current_node = None

    def add(self, number):
        self.current_node = AVLTree.add(self._f(number), self.current_node)
        return self.current_node

    def find(self, number):
        return 'Found' if AVLTree.find(self._f(number), self.current_node) else 'Not found'

    def remove(self, number):
        self.current_node = AVLTree.remove(self._f(number), self.current_node)
        return self.current_node

    def sum(self, l, r):
        if self.current_node is None:
            self.s = 0
        else:
            s = IntervalSet.interval(self._f(l), self._f(r), self.current_node)
            self.s = s if s else 0
        return self.s

    def _f(self, number):
        return (number + self.s) % 1000000001

    @staticmethod
    def cut_right(key, node):
        if node.right is None:
            return None
        if node.right.key >= key:
            return node.right
        return IntervalSet.cut_right(key, node.right)

    @staticmethod
    def cut_left(key, node):
        if node.left is None:
            return None
        if node.left.key <= key:
            return node.left
        return IntervalSet.cut_left(key, node.left)

    @staticmethod
    def add_lower_and_same_nodes(key, _sum, node):
        if node is None:
            return _sum
        if node.key > key:
            return IntervalSet.add_lower_and_same_nodes(key, _sum, node.left)
        else:
            _sum += node.sum
            _sum = IntervalSet.sub_over_nodes(key, _sum, node.right)
            return _sum

    @staticmethod
    def add_over_and_same_nodes(key, _sum, node):
        if node is None:
            return _sum
        if node.key < key:
            return IntervalSet.add_over_and_same_nodes(key, _sum, node.right)
        else:
            _sum += node.sum
            _sum = IntervalSet.sub_lower_nodes(key, _sum, node.left)
            return _sum

    @staticmethod
    def sub_over_nodes(key, _sum, node):
        if node is None:
            return _sum
        if node.key <= key:
            return IntervalSet.sub_over_nodes(key, _sum, node.right)
        else:
            _sum -= node.sum
            _sum = IntervalSet.add_lower_and_same_nodes(key, _sum, node.left)
            return _sum

    @staticmethod
    def sub_lower_nodes(key, _sum, node):
        if node is None:
            return _sum
        if node.key >= key:
            return IntervalSet.sub_lower_nodes(key, _sum, node.left)
        else:
            _sum -= node.sum
            _sum = IntervalSet.add_over_and_same_nodes(key, _sum, node.right)
            return _sum

    @staticmethod
    def sub_left(key, _sum, node):
        if node.key <= key:
            _sum -= node.sum
            return IntervalSet.add_over_and_same_nodes(key, _sum, node)
        if node.left is None:
            return _sum
        return IntervalSet.sub_left(key, _sum, node.left)

    @staticmethod
    def sub_right(key, _sum, node):
        if node.key >= key:
            _sum -= node.sum
            return IntervalSet.add_lower_and_same_nodes(key, _sum, node)
        if node.right is None:
            return _sum
        return IntervalSet.sub_right(key, _sum, node.right)

    @staticmethod
    def interval(left, right, node):
        if node is None:
            return 0
        if left <= node.key <= right:
            left_node = IntervalSet.cut_left(left, node)
            _sum = AVLTree.sum(node) - AVLTree.sum(left_node)
            _sum = IntervalSet.add_over_and_same_nodes(left, _sum, left_node)
            right_node = IntervalSet.cut_right(right, node)
            _sum = _sum - AVLTree.sum(right_node)
            _sum = IntervalSet.add_lower_and_same_nodes(right, _sum, right_node)
            return _sum
        elif node.key < left:
            sub_tree = IntervalSet.cut_right(left, node)
            if sub_tree is None:
                return 0
            _sum = IntervalSet.sub_lower_nodes(left, sub_tree.sum, sub_tree)
            return IntervalSet.sub_right(right, _sum, sub_tree)
        elif node.key > right:
            sub_tree = IntervalSet.cut_left(right, node)
            if sub_tree is None:
                return 0
            _sum = IntervalSet.sub_over_nodes(right, sub_tree.sum, sub_tree)
            return IntervalSet.sub_left(left, _sum, sub_tree)

    @staticmethod
    def in_order(node):
        ordered_list = []

        def crawler(node):
            if node is not None:
                crawler(node.left)
                ordered_list.append({'key': node.key, 'height': node.height, 'sum': node.sum})
                crawler(node.right)
        crawler(node)

        return ordered_list


def main():
    total = int(input())
    i_set = IntervalSet()
    for i in range(total):
        inp = input()
        if inp.startswith('+'):
            _, number = inp.split()
            i_set.add(int(number))
        elif inp.startswith('-'):
            _, number = inp.split()
            i_set.remove(int(number))
        elif inp.startswith('?'):
            _, number = inp.split()
            print(i_set.find(int(number)))
        elif inp.startswith('s'):
            _, l, r = inp.split()
            print(i_set.sum(int(l), int(r)))


if __name__ == '__main__':
    main()
