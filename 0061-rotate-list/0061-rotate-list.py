
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        # Handle empty list or a single node
        if not head or not head.next:
            return head

        # Find the length and the last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Avoid unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Connect the tail to the head (make a circle)
        tail.next = head

        # Find the new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # The next node becomes the new head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head
