from .maxProfit import printResult

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @printResult
    def middleNode(self, head: ListNode) -> ListNode:
        slowNode = head
        fastNode = head

        while(fastNode and fastNode.next):
            slowNode = slowNode.next
            fastNode = fastNode.next
            fastNode = fastNode.next

        return slowNode

if __name__ == '__main__':
    scanner = Solution()
    x = ListNode(1)
    scanner.middleNode(x)
    x.next = ListNode(2)
    scanner.middleNode(x)
    x.next.next = ListNode(3)
    scanner.middleNode(x)
    x.next.next.next = ListNode(4)
    scanner.middleNode(x)
    x.next.next.next.next = ListNode(5)
    scanner.middleNode(x)
