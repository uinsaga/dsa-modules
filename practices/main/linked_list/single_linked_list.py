class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, newData):
        newNode: Node = Node(newData)

        newNode.next = self.head
        self.head = newNode

    def addLast(self, newData):
        newNode: Node = Node(newData)

        node: Node = self.head

        while node.next is not None:
            node = node.next
            # print(node)

        node.next = newNode

    def addAtPoint(self, nodePoint: Node, newData):
        newNode = Node(newData)
        node: Node = self.head

        while node is not None:
            if node.next == nodePoint:
                node.next = newNode
                newNode.next = nodePoint
                # print("node found")
                break
            else:
                # print("not the node")
                node = node.next

    def deleteFirst(self):
        newHead = self.head.next
        self.head = newHead

    def deleteLast(self):
        node: Node = self.head

        while node.next is not None:
            node = node.next

        node.next = None

    def display(self):
        printVal: Node = self.head

        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next


# object SSL
l1 = SingleLinkedList()

## membuat head dengan node 1
l1.head = Node(1)

## membuat node 2
e2 = Node(2)

## membuat node 3
e3 = Node(3)

## mengisi data next dari node head dengan node e2
l1.head.next = e2

## mengisi data next dari node e3 dengan node e3
e2.next = e3

## menambahkan data pertama di depan head dengan -1
l1.addFirst(99)
l1.addAtPoint(e3, 800)
l1.addLast(100)

## menampilkan data linked list
print(f"display before delete head\n------------------\n")
l1.display()


l1.deleteFirst()
print("\ndisplay after delete head\n-------------------\n")
l1.display()

# l1.deleteLast()
# print("\ndisplay after delete last\n-------------------\n")
# l1.display()
