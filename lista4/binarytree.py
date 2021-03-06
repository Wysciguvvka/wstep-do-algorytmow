from __future__ import annotations


class ListNode:
    def __init__(self, data=None, _next=None) -> None:
        self.data = data
        self.next = _next


# FILO
class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data) -> None:
        new_node = ListNode(data)
        if self.head:
            current = self.head
            self.head = new_node
            self.head.next = current
        else:
            self.head = new_node

    def pop(self):
        current = None
        if self.head:
            current = self.head
            self.head = self.head.next
        return current.data if current else None

    @property
    def is_empty(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return True if not nodes else False

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)


# FIFO
class Queue:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data) -> None:
        new_node = ListNode(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def pop(self):
        current = None
        if self.head:
            current = self.head
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        return current.data if current else None

    @property
    def is_empty(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return True if not nodes else False

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)


class Node:
    """Klasa reprezentuj??ca w??ze?? drzewa binarnego."""

    def __init__(self, data=None, *, left: Node = None, right: Node = None, parent=None) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def height(self) -> int:
        _left = self.left.height if self.left is not None else 0
        _right = self.right.height if self.right is not None else 0
        # Return max(leftHeight, rightHeight) at each iteration
        return max(_left, _right) + 1

    def find_depth(self, node):
        if node is None or self is None:
            return 0

        if self == node:
            return 1
        if self.left:
            left = self.left.find_depth(node)
            if left != 0:
                return 1 + left
        if self.right:
            right = self.right.find_depth(node)
            if right != 0:
                return 1 + right
        return 0

    def bfs(self):
        q = Queue()  # Utworzenie kolejki
        q.insert(self)  # Dodanie pierwszego wierzcho??ka (korzenia) do kolejki
        while not q.is_empty:  # Dop??ki kolejka nie jest pusta
            node = q.pop()  # Pobranie elementu z kolejki
            print(node, end=' ')  # Wy??wietlenie go
            if node.left:
                q.insert(node.left)  # Dodanie do kolejki w??z??a z lewej strony (je??eli istnieje)
            if node.right:
                q.insert(node.right)  # Dodanie do kolejki w??z??a z prawej strony (je??eli istnieje)

    def dfs(self):
        stack = Stack()  # Utworzenie stosu
        stack.push(self)  # Dodanie pierwszego wierzcho??ka (korzenia) do stosu
        while not stack.is_empty:  # Dop??ki stos nie jest pusty
            node = stack.pop()  # Pobranie pierwszego elementu ze stosu
            print(node, end=' ')  # Wy??wietlenie go
            if node.right:
                stack.push(node.right)  # Dodanie do stosu w??z??a z prawej strony (je??eli istnieje)
            if node.left:
                stack.push(node.left)  # Dodanie do stosu w??z??a z lewej strony (je??eli istnieje)

    def count_nodes(self, k, *, level=1):

        # Base Case
        count = 0
        if self is None:
            return 0

        # Recursive Call for
        # the left subtree
        if self.left:
            count += self.left.count_nodes(k, level=level + 1)

        # Recursive Call for
        # the right subtree
        if self.right:
            count += self.right.count_nodes(k, level=level + 1)

        # If current level is
        # the required level
        if k == level:
            print(self.data, end=' ')
            count += 1
        return count

    def print_nodes(self, n: int):
        print(f'W??z??y na poziomie {n}:', end=' ')
        count = self.count_nodes(n)
        print(f'\nLiczba w??z????w na poziomie {n}: {count}')

    def print_all_nodes(self):
        for i in range(1, self.height + 1):
            print(f'W??z??y na poziomie {i}:', end=' ')
            count = self.count_nodes(i)
            print(f'\nLiczba w??z????w na poziomie {i}: {count}')

    @staticmethod
    def flip_binary_tree(root):
        if root is None:
            return root

        if root.left is None and root.right is None:
            return root

        flipped_tree = Node.flip_binary_tree(root.left)

        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None

        return flipped_tree

    @staticmethod
    def solve(root, leaf):
        def helper(node, new_par):
            if not node:
                return None
            if node == root:
                node.parent = new_par
                if node.left == new_par:
                    node.left = None
                if node.right == new_par:
                    node.right = None
                return root
            if node.left:
                node.right = node.left
            if node.parent.left == node:
                node.parent.left = None
            node.left = helper(node.parent, node)
            node.parent = new_par
            return node

        return helper(leaf, None)

    def min_depth_leaves(self):
        q = Queue()
        q.insert(self)
        min_depth = None
        leaves = []
        while not q.is_empty:
            node = q.pop()
            if not node.left and not node.right:
                __depth = self.find_depth(node)
                if not min_depth:
                    min_depth = __depth
                if min_depth >= __depth:
                    leaves.append(node.data)
            if node.left:
                q.insert(node.left)
            if node.right:
                q.insert(node.right)
        print(f'D??ugo???? najkr??tszej ??cie??ki: {min_depth}'
              f'\nLi??cie znajduj??ce si?? na g????boko????i {min_depth}: {" ".join(leaves)}')

    def __repr__(self) -> str:
        return str(self.data)


if __name__ == '__main__':
    print("Z1")
    _root = Node(1)
    _root.left = Node(2, parent=_root)
    _root.right = Node(3, parent=_root)
    _root.left.left = Node(4, parent=_root.left)
    _root.left.left.left = Node(8, parent=_root.left.left)
    _root.left.right = Node(5, parent=_root.left)
    _root.right.left = Node(6, parent=_root.right)
    _root.right.right = Node(7, parent=_root.right)
    # Struktura drzewa binarnego
    #            1
    #         /     \
    #        2       3
    #      /   \    /  \
    #     4     5  6    7
    #    /
    #   8
    print(f'Wysoko???? drzewa: {_root.height}')
    print('---')
    print('przeszukiwanie BFS:')
    _root.bfs()
    print('\n---')
    print('przeszukiwanie DFS:')
    _root.dfs()
    print('\n---')
    """Z2"""
    print("Z2:\ndrzewo pocz??tkowe:")
    _root.print_all_nodes()
    leaf_root = Node.solve(_root, _root.right.right)
    print('\nDrzewo z korzeniem jako li???? "8":\n8')
    leaf_root.print_all_nodes()
    print('---')
    """Z3"""
    print("Z3")
    tree = Node("A")
    tree.left = Node("B")
    tree.right = Node("C")
    tree.left.left = Node("D")
    tree.left.right = Node("E")
    tree.left.left.left = Node("F")
    # Struktura drzewa binarnego
    #            A
    #         /     \
    #        B       C
    #      /   \
    #     D     E
    #    /
    #   F
    # tree.print_nodes(3)
    # print('---')
    tree.print_all_nodes()
    print('---')
    tree.min_depth_leaves()
    print('---')
