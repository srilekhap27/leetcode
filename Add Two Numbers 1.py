class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, over=0) -> ListNode:
        if l1 is None and l2 is None:
            if over > 0:
                return ListNode(over)
            return None
        
        num = over
        next1 = None
        next2 = None
        
        if not l1 is None:
            num += l1.val
            next1 = l1.next
        
        if not l2 is None:
            num += l2.val
            next2 = l2.next
        
        node = ListNode(num)
        over = 0
        if node.val > 9:
            over = 1
            node.val -= 10
        
        node.next = self.addTwoNumbers(next1, next2, over)
        
        return node