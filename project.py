from typing import Any


class Node: # Tworzenie wezła Node
    def __init__(self, data):
        self.data = data #wartosc
        self.next = None #nastepny element


class LinkedList:
    def __init__(self):
        self.head = None #tworzenie pustej listy
        self.tail = None # ostatni element tzw ogon

    def __str__(self): # jak jest print to wypisuje wszystkie elementy listy
        tekst = "" # tekst jes pusty
        pom = self.head # przyisuje dodatkowa wartosc
        while pom is not None: # po kolei po elementach
            tekst += str(pom.data) # dodanie wartosci  do str
            pom = pom.next # przejscie do nastepnego elementy
            if pom is not None:
                tekst += " -> " # dodanie strzaleczki #musi byc bo asert wywali blad
        return tekst # zwracanie tekstu

    def __len__(self): # zwraca dlugosc listy
        if self.head is None:
            return 0
        pom = self.head #
        licznik = 0
        while pom is not None: # dopoki lista jest pusta to przesuwamy do nastepnego elementu
            pom = pom.next
            licznik += 1
        return licznik

    def push(self, value: Any) -> None:
        nowa_w = Node(value) #nowy wezel
        nowa_w.next = self.head # dodaje przed poprzednia
        self.head = nowa_w # nowa wartosc nowa glowa

    def append(self, value: Any) -> None:
        nowa_w = Node(value) # tworzenie nowego wezlu
        if self.head is None:
            self.head = nowa_w # jesli lista jest pusta to glowa bedzie nowy element
            return
        pom = self.head
        while pom.next:
            pom = pom.next
        pom.next = nowa_w

    def node(self, at: int) -> None:
        wuwu = self.head # przypisanie zmiennej jako glowy
        for i in range(at):
            wuwu = wuwu.next
        return wuwu

    def insert(self, value: Any, after: Node) -> None:
        nowa_w = Node(value)
        nowa_w.next = after.next #wprowadzasz po jakim wezle chcesz to nadac
        after.next = nowa_w

    def pop(self) -> Any:
        pom = self.head
        self.head = pom.next
        return pom.data



    def remove(self, after: Node) -> Any:
        if after.next is None:
            print("Wskazany wezel nie znajduje sie w liscie.")
            return
        else:
         after.next = after.next.next



list_ = LinkedList()

assert list_.head == None

list_.push(1) # dodaje 1 jako nastepny
list_.push(0) # 0 dodaje jako kolejny elelemtn

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'


middle_node = list_.node(at=1) # 16

list_.insert(5, after=middle_node) # 1 5 6 dodanie 5

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'


first_element = list_.node(at=0)
returned_first_element = list_.pop() # usuwa pierwszy elelemtn

assert first_element.data == returned_first_element


print(list_)
print(len(list_))


class LinkedList:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self): # wszystkie elelemtny stosu
        txt = ""
        pom = self.head.next
        while pom is not None:
            txt += str(pom.data) #dodanie kolejnego ellemntu
            pom = pom.next
            if pom is not None:
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
            self.tail = self.head # jesli jest jedna wartosc to jest tym i tym
        else:
            self.tail.next = dod # nastepny element to nasza wartoc
            self.tail = self.tail.next #ogon to nasza nowa wartosc
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