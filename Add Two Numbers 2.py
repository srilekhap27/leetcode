class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
		# loop through the first linked list, storing the values in the num1 variable
        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next
		# follows same process as above
        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next
		# calculate the sum of the values that we just obtained and store it as a string
        summation = str(int(num1) + int(num2))
		# make the head of the node the first number in the summation string
        head = ListNode(summation[0])
		# create a new reference to the head so we can manipulate the linked list but not lose the original reference to the head
        temp = head
		# loop through the remaining numbers in the summation string, each time creating a new node
        for val in summation[1:]:
            temp.next = ListNode(val)
            temp = temp.next
		# return the original reference to the head
        return head