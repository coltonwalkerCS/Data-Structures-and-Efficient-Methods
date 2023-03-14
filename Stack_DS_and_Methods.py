from LinkedList_DS_and_Methods import LinkedList, Node


class FIFO_Stack:

    def __init__(self):
        self.llist = LinkedList()
        # self.llist.head = None
        self.endNode = None
        self.size = 0

    def push(self, data):
        newNode = Node(data)

        if self.size == 0:
            self.llist.head = newNode
            self.endNode = newNode
            self.size += 1
        else:
            self.endNode.next = newNode
            self.endNode = newNode
            self.size += 1

    def pop(self):
        if not self.size:
            print("Error")
        else:
            value = self.llist.head.data
            self.llist.head = self.llist.head.next
            self.size -= 1
            return value

    def isEmpty(self):
        return bool(self.size)

    def print(self):
        print(self.size)
        temp = self.llist.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        return


FIFOSTACK = FIFO_Stack()
FIFOSTACK.push(1)
FIFOSTACK.push(2)
FIFOSTACK.push(3)
print(FIFOSTACK.print())
