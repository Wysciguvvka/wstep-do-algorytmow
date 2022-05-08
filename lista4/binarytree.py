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
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, *, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left
        self.right = right

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
        q.insert(self)  # Dodanie pierwszego wierzchołka (korzenia) do kolejki
        while not q.is_empty:  # Dopóki kolejka nie jest pusta
            node = q.pop()  # Pobranie elementu z kolejki
            print(node, end=' ')  # Wyświetlenie go
            if node.left:
                q.insert(node.left)  # Dodanie do kolejki węzła z lewej strony (jeżeli istnieje)
            if node.right:
                q.insert(node.right)  # Dodanie do kolejki węzła z prawej strony (jeżeli istnieje)

    def dfs(self):
        stack = Stack()  # Utworzenie stosu
        stack.push(self)  # Dodanie pierwszego wierzchołka (korzenia) do stosu
        while not stack.is_empty:  # Dopóki stos nie jest pusty
            node = stack.pop()  # Pobranie pierwszego elementu ze stosu
            print(node, end=' ')  # Wyświetlenie go
            if node.right:
                stack.push(node.right)  # Dodanie do stosu węzła z prawej strony (jeżeli istnieje)
            if node.left:
                stack.push(node.left)  # Dodanie do stosu węzła z lewej strony (jeżeli istnieje)

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
        print(f'Węzły na poziomie {n}:', end=' ')
        count = self.count_nodes(n)
        print(f'\nLiczba węzłów na poziomie {n}: {count}')

    def print_all_nodes(self):
        for i in range(1, self.height + 1):
            print(f'Węzły na poziomie {i}:', end=' ')
            count = tree.count_nodes(i)
            print(f'\nLiczba węzłów na poziomie {i}: {count}')

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
        print(f'Długość najkrótszej ścieżki: {min_depth}'
              f'\nLiście znajdujące się na głębokośći {min_depth}: {" ".join(leaves)}')

    def __repr__(self) -> str:
        return str(self.data)


if __name__ == '__main__':
    _root = Node(1)
    _root.left = Node(2)
    _root.right = Node(3)
    _root.left.left = Node(4)
    _root.left.left.left = Node(8)
    _root.left.right = Node(5)
    _root.right.left = Node(6)
    _root.right.right = Node(7)
    print(f'Wysokość drzewa: {_root.height}')
    print('---')
    print('przeszukiwanie BFS:')
    _root.bfs()
    print('\n---')
    print('przeszukiwanie DFS:')
    _root.dfs()
    print('\n---')
    """Z3"""
    tree = Node("A")
    tree.left = Node("B")
    tree.right = Node("C")
    tree.left.left = Node("D")
    tree.left.right = Node("E")
    tree.left.left.left = Node("F")
    # tree.print_nodes(3)
    # print('---')
    tree.print_all_nodes()
    print('---')
    tree.min_depth_leaves()
