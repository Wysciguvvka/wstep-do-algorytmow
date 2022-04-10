import random
from copy import deepcopy


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
    def __init__(self, *, length=40, tsorted=None) -> None:
        self.length = length
        self.queue = LinkedList()
        self.sorted = tsorted
        self.__list = []
        self.init_queue(length)

    def init_queue(self, length) -> None:
        for i in range(0, length):
            _type = random.choice([Counter.A, Counter.B, Counter.C])
            complexity = random.randint(_type, _type + 3)
            self.__list.append((_type, complexity))
            if not self.sorted:
                self.queue.insert((_type, complexity))
        if self.sorted:
            if self.sorted == 1:
                """Rosnąco"""
                self.__list = sorted(self.__list, key=lambda tup: tup[1], reverse=False)
                for _item in self.__list:
                    self.queue.insert(_item)
                return
            if self.sorted == 2:
                """malejąco"""
                self.__list = sorted(self.__list, key=lambda tup: tup[1], reverse=True)
                for _item in self.__list:
                    self.queue.insert(_item)
                return


class Bureaucracy:
    def __init__(self, *, a, b, c, e, queue=Queue(), desc="Urząd") -> None:
        self.counters = []
        self.init_counters(a=a, b=b, c=c, e=e)
        self.queue = queue
        self.iter = 0
        self.desc = desc
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

    def do_tasks(self) -> None:
        finished = False
        while not finished:
            finished = True
            self.iter += 1
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

    def print_data(self):
        print(f'Liczba wykonanych iteracji dla urzędu typu {self.desc}: {self.iter}')

    def get_iter(self) -> int:
        return self.iter

    def __repr__(self) -> str:
        return self.desc

    def __str__(self) -> str:
        return self.desc


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    q = Queue(length=30)
    q1 = deepcopy(q)
    q2 = deepcopy(q)
    q3 = deepcopy(q)
    q4 = deepcopy(q)
    office1 = Bureaucracy(a=3, b=3, c=3, e=1, queue=q1, desc="Domyślny")  # domyslna
    office2 = Bureaucracy(a=3, b=3, c=3, e=0, queue=q2, desc="9 okienek")  # 9 okienek 0 ekspertów
    office3 = Bureaucracy(a=2, b=2, c=2, e=3, queue=q3, desc="3 ekspertów")  # 3 ekspertow
    office4 = Bureaucracy(a=1, b=2, c=3, e=1, queue=q4, desc="7 okienek")  # 7 okienek
    office1.print_data()
    office2.print_data()
    office3.print_data()
    office4.print_data()
    print('\n---\n')
    office_data = []
    for _ in range(100):
        q = Queue(length=random.randint(10, 40))
        q1 = deepcopy(q)
        q2 = deepcopy(q)
        office1 = Bureaucracy(a=3, b=3, c=3, e=1, queue=q1, desc="Domyślny")
        office2 = Bureaucracy(a=2, b=2, c=2, e=3, queue=q2, desc="3 ekspertów")
        _data = {
            "Urzad 1": office1.get_iter(),
            "Urzad 2": office2.get_iter()
        }
        office_data.append(_data)

    occ1 = [_dt["Urzad 1"] for _dt in office_data]
    occ2 = [_dt["Urzad 2"] for _dt in office_data]
    print(
        f'Lista nieposortowana - średni czas oczekiwania:'
        f'\n\tUrząd1:{sum(occ1) / len(occ1)}\n\tUrząd2:{sum(occ2) / len(occ2)}')
    plt.figure("nieposortowana lista")
    bins = max([max(occ1) - min(occ1), max(occ2) - min(occ2)])
    plt.hist(occ1, bins, stacked=True, label="9 Kolejek 1 E", alpha=0.8, color="blue")
    plt.hist(occ2, bins, stacked=True, label="9 kolejek 3 E", alpha=0.8, color="green")
    plt.legend()
    plt.xlabel("Iteracje")
    plt.ylabel("Częstość występowania")
    plt.title("Nieposortowana lista - Histogram")
    plt.show()

    for _ in range(100):
        q = Queue(length=random.randint(10, 40), tsorted=1)
        q1 = deepcopy(q)
        q2 = deepcopy(q)
        office1 = Bureaucracy(a=3, b=3, c=3, e=1, queue=q1, desc="Domyślny")
        office2 = Bureaucracy(a=2, b=2, c=2, e=3, queue=q2, desc="3 ekspertów")
        _data = {
            "Urzad 1": office1.get_iter(),
            "Urzad 2": office2.get_iter()
        }
        office_data.append(_data)

    occ1 = [_dt["Urzad 1"] for _dt in office_data]
    occ2 = [_dt["Urzad 2"] for _dt in office_data]
    plt.figure("Posortowana lista rosnąco")
    print(
        f'Lista posortowana rosnąco - średni czas oczekiwania:'
        f'\n\tUrząd1:{sum(occ1) / len(occ1)}\n\tUrząd2:{sum(occ2) / len(occ2)}')
    bins = max([max(occ1) - min(occ1), max(occ2) - min(occ2)])
    plt.hist(occ1, bins, stacked=True, label="9 Kolejek 1 E", alpha=0.8, color="blue")
    plt.hist(occ2, bins, stacked=True, label="9 kolejek 3 E", alpha=0.8, color="green")
    plt.legend()
    plt.xlabel("Iteracje")
    plt.ylabel("Częstość występowania")
    plt.title("Lista posortowana rosnąco - Histogram")
    plt.show()

    for _ in range(100):
        q = Queue(length=random.randint(10, 40), tsorted=2)
        q1 = deepcopy(q)
        q2 = deepcopy(q)
        office1 = Bureaucracy(a=3, b=3, c=3, e=1, queue=q1, desc="Domyślny")
        office2 = Bureaucracy(a=2, b=2, c=2, e=3, queue=q2, desc="3 ekspertów")
        _data = {
            "Urzad 1": office1.get_iter(),
            "Urzad 2": office2.get_iter()
        }
        office_data.append(_data)

    occ1 = [_dt["Urzad 1"] for _dt in office_data]
    occ2 = [_dt["Urzad 2"] for _dt in office_data]
    print(
        f'Lista posortowana malejąco - średni czas oczekiwania:'
        f'\n\tUrząd1:{sum(occ1) / len(occ1)}\n\tUrząd2:{sum(occ2) / len(occ2)}')
    plt.figure("Posortowana lista malejąco")
    bins = max([max(occ1) - min(occ1), max(occ2) - min(occ2)])
    plt.hist(occ1, bins, stacked=True, label="9 Kolejek 1 E", alpha=0.8, color="blue")
    plt.hist(occ2, bins, stacked=True, label="9 kolejek 3 E", alpha=0.8, color="green")
    plt.legend()
    plt.xlabel("Iteracje")
    plt.ylabel("Częstość występowania")
    plt.title("Lista posortowana malejąco - Histogram")
    plt.show()
