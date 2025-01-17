
# Time Complexity : O(n)
# Space Complexity : O(1);
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy
        count = 0
        while (count <= n):
            fast = fast.next
            count += 1
        while(fast != None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
        
