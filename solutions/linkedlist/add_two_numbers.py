from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode(0)
        curr = res_head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            s = l1_val + l2_val + carry
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res_head.next


if __name__ == '__main__':
    num1 = ListNode(2)
    num1.next = ListNode(4)
    num1.next.next = ListNode(3)
    num1.next.next.next = ListNode(9)

    num2 = ListNode(5)
    num2.next = ListNode(6)
    num2.next.next = ListNode(4)
    num2.next.next.next = ListNode(5)
    res_head = Solution().addTwoNumbers(num1, num2)
    while res_head:
        print(res_head.val, end="")
        res_head = res_head.next
