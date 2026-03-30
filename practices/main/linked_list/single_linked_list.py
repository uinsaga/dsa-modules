class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList():
    def __init__(self):
        self.head = None

    def addFirst(self, newData):
         newNode:Node = Node(newData)

         newNode.next = self.head
         self.head = newNode

    def addLast(self):
        print("add last")

    def addAtPoint(self, newData):
        print("insert data")

    def deleteFirst(self):
        print("delete first")

    def deleteLast():
        print("delete last")

    def display(self):
        printVal:Node = self.head

        while(printVal is not None):
            print(printVal.data)
            printVal = printVal.next



# object SSL
l1 = SingleLinkedList()

## membuat head dengan node 1
l1.head = Node("1")

## membuat node 2
e2 = Node(2)

## membuat node 3
e3  = Node(3)

## mengisi data next dari node head dengan node e2
l1.head.next = e2

## mengisi data next dari node e3 dengan node e3
e2.next = e3

## menambahkan data pertama di depan head dengan -1
l1.addFirst(99)
l1.addFirst(100)

## menampilkan data linked list
l1.display()