import random


class Node:
    def __init__(self, data=None, _next=None) -> None:
        self.data = data
        self.next = _next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data) -> None:
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def search_item(self, x) -> Node | None:
        if self.head is None:
            return
        n = self.head
        while n is not None:
            if n.data[0] == x:
                return n
            n = n.next
        return None

    def delete(self, data) -> None:
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("There is no such a element in the list!")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next


class Task:
    def __init__(self, _type, complexity: int) -> None:
        self.type = _type
        self.complexity = complexity


class Counter:
    A = 1
    B = 5
    C = 9
    E = None

    def __init__(self) -> None:
        self.task = None
        self.clients = 0
        self.time = 0

    def take_task(self, task) -> None:
        self.clients += 1
        self.task = task
        self.time = task[1]

    def do_task(self) -> None:
        if not self.time:
            self.task = None
            self.time = 0
            return
        self.time -= 1

    def __repr__(self) -> str:
        return type(self).__name__

    def __str__(self) -> str:
        return type(self).__name__


class A(Counter):
    def __init__(self) -> None:
        Counter.__init__(self)
        self.acceptedType = Counter.A


class B(Counter):
    def __init__(self) -> None:
        Counter.__init__(self)
        self.acceptedType = Counter.B


class C(Counter):
    def __init__(self) -> None:
        Counter.__init__(self)
        self.acceptedType = Counter.C


class E(Counter):
    def __init__(self) -> None:
        Counter.__init__(self)
        self.acceptedType = Counter.E


class Queue:
    def __init__(self, length=40) -> None:
        self.queue = LinkedList()
        self.init_queue(length)

    def init_queue(self, length) -> None:
        for i in range(0, length):
            _type = random.choice([Counter.A, Counter.B, Counter.C])
            complexity = random.randint(_type, _type + 3)
            self.queue.insert((_type, complexity))


class Bureaucracy:
    def __init__(self, *, a, b, c, e, queue=Queue()) -> None:
        self.counters = []
        self.init_counters(a=a, b=b, c=c, e=e)
        self.queue = queue
        self.do_tasks()

    def init_counters(self, *, a, b, c, e) -> None:
        for counter in range(0, a):
            _counter = A()
            self.counters.append([_counter, _counter.time])
        for counter in range(0, b):
            _counter = B()
            self.counters.append([_counter, _counter.time])
        for counter in range(0, c):
            _counter = C()
            self.counters.append([_counter, _counter.time])
        for counter in range(0, e):
            _counter = E()
            self.counters.append([_counter, _counter.time])
        print(self.counters)

    def do_tasks(self) -> None:
        finished = False
        _iter = 0
        while not finished:
            finished = True
            _iter += 1
            for counter in self.counters:
                if counter[0].task:
                    finished = False
                    counter[0].do_task()
                    counter[1] = counter[0].time
                if counter[0].time <= 0 or not counter[0].task:
                    task = self.queue.queue.search_item(counter[0].acceptedType) if counter[0].acceptedType \
                        else self.queue.queue.head
                    if task:
                        counter[0].take_task(task.data)
                        counter[1] = task.data[1]
                        self.queue.queue.delete(task.data)
                        finished = False
        print(f'Liczba wykonanych iteracji: {_iter}')
        for i, counter in enumerate(self.counters):
            print(f'liczba obsłużonych klientów dla okienka {i + 1}: {counter[0].clients}')


if __name__ == '__main__':
    q = Queue(length=40)
    Bureaucracy(a=3, b=3, c=3, e=1, queue=q)
