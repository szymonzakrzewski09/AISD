from typing import Any

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        txt = ""
        dod = self.head
        while dod is not None:
            txt += str(dod.data)
            dod = dod.next
            if dod is not None:
                txt += " -> "
        return txt

    def __len__(self):
        if self.head is None:
            return 0
        dod = self.head
        licznik = 0
        while dod is not None:
            dod = dod.next
            licznik += 1
        return licznik

    def push(self, value: Any) -> None:
        new_w = Node(value)
        new_w.next = self.head
        self.head = new_w

    def append(self, value: Any) -> None:
        nowy_w = Node(value)
        if self.head is None:
            self.head = nowy_w
            return
        dod = self.head
        while dod.next:
            dod = dod.next
        dod.next = nowy_w

    def node(self, at: int) -> None:
        wezel_w = self.head
        for i in range(at):
            wezel_w = wezel_w.next
        return wezel_w

    def insert(self, value: Any, after: Node) -> None:
        nowy_ww = Node(value)
        nowy_ww.next = after.next
        after.next = nowy_ww

    def pop(self) -> Any:
        dod = self.head
        self.head = dod.next
        return dod.data



    def remove(self, after: Node) -> Any:
        if after.next is None:
            print("Bład.Podany węzeł nie istnieje.")
            return
        else:
         after.next = after.next.next



list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'


middle_node = list_.node(at=1)

list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'


first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.data == returned_first_element


print(list_)
print(len(list_))


class LinkedList:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        txt = ""
        dod = self.head.next
        while dod is not None:
            txt += str(dod.data)
            dod = dod.next
            if dod is not None:
                txt += " \n"
        return txt

    def push(self, element: Any) -> None:
        new = Node(element)
        new.next = self.head.next
        self.head.next = new
        self.size += 1

    def pop(self) -> Any:
        usun = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return usun.data
class Stack(LinkedList):
    pass

stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2

print(stack)
print("liczba elementow stosu: ", len(stack))


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        txt = ""
        dod = self.head
        while dod is not None:
            txt += str(dod.data)
            dod = dod.next
            if dod is not None:
                txt += ", "
        return txt

    def __len__(self):
        return self.size

    def peek(self) -> Any:
        return self.head.data

    def enqueue(self, element: Any) -> None:
        dod = Node(element)
        if self.tail is None:
            self.head = dod
            self.tail = self.head
        else:
            self.tail.next = dod
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> None:
        dod = self.head
        self.head = self.head.next
        self.size -= 1
        return dod.data


queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2