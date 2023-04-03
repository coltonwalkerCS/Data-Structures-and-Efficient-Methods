from LinkedList_DS_and_Methods import LinkedList, Node


class FIFO_Stack:

    def __init__(self):
        self.front = self.back = None
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        self.size += 1

        if self.back is None:
            self.front = self.back = newNode
            return
        self.back.next = newNode
        self.back = newNode

    def pop(self):
        if not self.size:
            print("Error")
        else:
            value = self.front.data
            self.front = self.front.next
            self.size -= 1
            return value

    def isEmpty(self):
        return bool(self.size)

    def print(self):
        print(self.size)
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print('')
        return


FIFOSTACK = FIFO_Stack()
FIFOSTACK.push(1)
FIFOSTACK.push(2)
FIFOSTACK.push(3)
FIFOSTACK.pop()
FIFOSTACK.pop()
FIFOSTACK.print()
