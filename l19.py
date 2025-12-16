## beats 100% of all solutins

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        runner = head
        count = 0
        while runner!= None:
            count+=1
            runner = runner.next
        if count == 1: return None
        if count == n: return head.next
        reach = count-n
        runner = head  
        while reach>1:
     
            runner = runner.next
            reach-=1
       
        
        runner.next = runner.next.next
        return head
        
