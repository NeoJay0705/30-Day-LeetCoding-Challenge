from .maxProfit import printResult

class Node:
    def __init__(self, x):
        self.val = x
        self.minVal = x
        self.next = None

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head: Node = None

    def push(self, x: int) -> None:
        if x is not None:
            if not self.head:
                self.head = Node(x)
            else:
                newNode = Node(x)
                newNode.next = self.head
                self.head = newNode

    def pop(self) -> None:
        if self.head:
            delNode = self.head
            self.head = self.head.next

    @printResult
    def top(self) -> int:
        if self.head:
            return self.head.val
        return None

    @printResult
    def getMin(self) -> int:
        if self.head:
            minNumber = self.head.val
            tmpNode = self.head
            while tmpNode:
                if minNumber > tmpNode.val:
                    minNumber = tmpNode.val
                tmpNode = tmpNode.next

            return minNumber
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    scanner = MinStack()
    scanner.top()
    scanner.pop()
    scanner.push(None)
    scanner.push(1)
    scanner.getMin()
    scanner.push(2)
    scanner.push(3)
    scanner.pop()
    scanner.top()
    scanner.getMin()
