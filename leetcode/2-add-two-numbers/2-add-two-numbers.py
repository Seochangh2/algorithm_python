# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nums1 = []
        nums2 = []
        nums3 = []
        def makeNums(node , nums):
            if not node:
                return
            else:
                makeNums(node.next,nums)
                nums.append(node.val)
                return
        
        def calculateNums(nums):
            num=0
            for i in range(len(nums)):
                num += nums[i]*(10**(len(nums) - i-1))
            return num     
        
        def makeList(num,nums):
            count = 1
            while math.trunc(num / (10**(count-1))) >0:
                nums.append(math.trunc( (num % 10**count)/10**(count-1) ) )
                pre = num % 10**count
                count +=1
                
            
        makeNums(l1,nums1)
        makeNums(l2,nums2)
        
        num1 = calculateNums(nums1)
        num2 = calculateNums(nums2)

        num3 = num1+num2
        makeList(num3 , nums3)

        
        node = ListNode()
        head = node
        
        for i in range(len(nums3)):
            node.val=nums3[i]
            if i != len(nums3)-1:
                node.next = ListNode()
                node = node.next
                
        
        
        
        return head
        
            