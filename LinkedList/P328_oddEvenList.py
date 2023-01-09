# Definition for singly-linked list.
from typing import Optional
from LinkedList.createListNode import ListNode, create_listnode_from_list


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        p1 = head
        p2 = head.next
        even_head = head.next

        while p2.next and p2.next.next:
            p1.next = p2.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next

        if p2.next:
            p1.next = p2.next
            p2.next = None
            p1 = p1.next

        p1.next = even_head
        return head


if __name__ == '__main__':
    head = create_listnode_from_list([1, 2, 3, 4, 5])
    new_head = Solution().oddEvenList(head)
    while new_head.next:
        print(new_head.val, end=' ')
