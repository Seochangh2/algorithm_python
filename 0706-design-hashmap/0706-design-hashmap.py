class ListNode:
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.next = None

class MyHashMap(object):
    
    def __init__(self):
        self.hashMap = collections.defaultdict(ListNode)
        self.size = 1000
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size
        if self.hashMap[index] is None :
            self.hashMap[index] = ListNode(key,value)
            return
        else :
            pointer = self.hashMap[index]
            while pointer:
                if pointer.key == key:
                    pointer.val = value
                    return
                elif pointer.next is None:
                    break
                pointer = pointer.next

            pointer.next = ListNode(key,value)
            return

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.size
        if self.hashMap[index] is None:
            return -1
        else:
            pointer = self.hashMap[index]
            while pointer:
                if pointer.key == key:
                    return pointer.val
                elif pointer.next is None:
                    break
                pointer = pointer.next
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size
        if self.hashMap[index] is None:
            return
        else:
            pointer = self.hashMap[index]
            if pointer.key == key:
                self.hashMap[index] = pointer.next
                return
            
            while pointer and pointer.next :
                if pointer.next.key == key:
                    pointer.next = pointer.next.next
                elif pointer.next.next is None:
                    break
                pointer = pointer.next

            return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)