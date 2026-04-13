class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PlayList:
    def __init__(self):
        self.head = None

    def insertOnHead(self, data):
        newNode: Node = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertOnTheLast(self, data):
        newNode: Node = Node(data)

        node = self.head

        while node is not None:
            if node.next is None:
                node.next = newNode
                break
            else:
                node = node.next

    def insertAfterKey(self, keyNode, data):
        newNode = Node(data)

        node:Node = self.head

        while node is not None:
            print(node.data, keyNode.data)
            if node == keyNode:
                newNode.next = node.next
                node.next = newNode
                break
            else:
                node = node.next

    def showData(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


tarotSong = Node("Tarot Song")
tendaBiru = Node("Tenda Biru")
selimutTetangga = Node("Selimut Tetangga")

pl = PlayList()
pl.head = tarotSong
tarotSong.next = tendaBiru
tendaBiru.next = selimutTetangga

# pl.insertOnHead("Madu Tiga")
# pl.insertOnTheLast("Madu Lima")
# pl.insertOnTheLast("Madu Enam")
pl.insertAfterKey(tendaBiru, "Madu satu")
pl.showData()
