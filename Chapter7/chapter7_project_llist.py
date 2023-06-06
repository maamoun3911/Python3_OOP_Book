class Cursor:
    def __init__(self) -> None:
        self.cursor: int = 0
    
    # def __repr__(self) -> str:
    #     return f"{self.cursor}"

class LinkedList:
    def __init__(self, nodes = None) -> None:
        self.head = None
        index = 0
        if nodes:
            node: Node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next
                index += 1
                node.index = index
    
    def __index(self, idx):
        """
        helper method to find given index
        """
        length = len(self)
        if length <= idx or length < -idx:
            raise IndexError("index out of range")
        elif -length <= idx < 0:
            idx = length+idx
        return idx

    def __get(self, index: int):
        """
        uses __index() to find index and return value of it
        """
        index = self.__index(index)
        head_node, idx, result = self.head, 0, None
        while head_node:
            if idx == index:
                result = head_node.data, head_node
            idx, head_node = idx+1, head_node.next
        return result

    def get_element(self, index: int):
        """
        a method to find linked-list element by index using __get()
        """
        return self.__get(index)[0]
        
    def set_element(self, index, value):
        """
        a method to find linked-list element by index and change it's value
        """
        node = self.__get(index)[1]
        node.data = value
    
    def __normal_traverse(self, new_node):
        """
        traverse through linked list and insert specific value in the index position
        """
        pre, nxt = self.head, self.head
        while nxt:
            if nxt.index == new_node.index:
                new_node.next = nxt
                pre.next = new_node
                break
            pre, nxt = nxt, nxt.next
    
    def __index_process(self, idx):
        """
        a way to figure if:
        - the index isn't in the linked list so we raise IndexError
        - or index is there but a negative number so we procces it
        - we return proccesses index and length for efficient and DRY reasons
        """
        length = len(self)
        if length < idx or length < -idx:
            raise IndexError("index out of range")
        elif -length <= idx < 0: # -length <= idx < 0
            idx = length+idx
        return idx, length
    
    def _up(self, index, node=None):
        if not node:
            node = self.head
        while node:
            if node.index == index:
                node.index, index = node.index+1, index+1
            node = node.next
    
    def insert_at_begging(self, node):
        node.next = self.head
        self.head = node
        self._up(0, self.head.next)
    
    def __insertion_status(self, index: int, value):
        """
        first this method uses __index_process
        then:
        if the index is 0 => just assign self.head to next element
        if the index is the last index we use __last_traverse() to find last element
        if index is in middle of linked list then we call __normal_traverse 
        and do the insertion process
        """
        index, length = self.__index_process(index)
        node = Node(value, index=index)
        if index == 0:
            self.insert_at_begging(node)
        elif index == length:
            self.__last_traverse(node)
        else:
            self.__normal_traverse(node)
            self._up(index, node.next)

    def insert(self, index: int, value):
        """
        inserting input value to specific index in the linked list
        using __insertion_status()
        """
        index = self.__insertion_status(index, value)


    def __last_traverse(self, node):
        "helper method that return the last element"
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node
    
    def append(self, value):
        """
        creating Node(value) and append to linked list
        using __last_traverse()
        """
        last_node = self.__last_traverse()
        last_node.next = Node(data=value, index=last_node.index+1)
    
    def sort(self):
        """
        just sorting, comparison depending on __lt__ __eq__ __gt__ methods in Node class
        """
        for _ in range(len(self)):
            pre, nxt = self.head, self.head.next
            while nxt:
                if pre > nxt:
                    pre.data, nxt.data = nxt.data, pre.data
                pre, nxt = pre.next, nxt.next
    
    def index(self, value):
        """
        a method to find the index of the given value
        """
        head_node = self.head
        while head_node:
            if value == head_node.data:
                return head_node.index
            head_node = head_node.next
        raise ValueError("No such value")

    def _down(self, replaced_node: int):
        node = self.head
        while node:
            if replaced_node.index == node.index:
                node.index = node.index-1
            node = node.next

    def pop_from_middle_last(self, index):
        pre, nxt = self.head, self.head
        while nxt:
            if index == nxt.index:
                pre.next = nxt.next
                break
            pre, nxt = nxt, nxt.next
        self._down(pre.next)

    def pop(self, index: int):
        """
        first we validate if index is available via __index()
        then we check the index place and pop demanded item
        """
        index = self.__index(index)
        if index == 0:
            self.head = self.head.next
            self._down(1)
        else:
            self.pop_from_middle_last(index)

    def delete(self, value):
        pre, nxt = self.head, self.head
        while nxt:
            if nxt.data == value:
                if nxt.index == 0:
                    self.head = self.head.next
                else:
                    pre.next = nxt.next
                self._down(pre.next.index)
                break
            pre, nxt = nxt, nxt.next
        else:
            raise ValueError("No such value to delete")

    def __len__(self) -> int:
        head_node = self.head
        length: int = 0
        while head_node:
            length += 1
            head_node = head_node.next
        return length
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        # return self
        head_node = self.head
        while head_node:
            yield head_node
            head_node = head_node.next

    # def __next__(self):
        # while self.ne:
        #     cache = self.ne
        #     if cache:
        #         self.ne = self.ne.next
        #     return cache
        # raise StopIteration


class Node:
    def __init__(self, data, nxt=None, index: int = 0) -> None:
        self.data = data
        self.next = nxt
        self.index = index

    def __repr__(self) -> str:
        return f"node val:{self.data}, node index: {self.index}"
    
    def __lt__(self, object):
        """
        a method to define "<" operator
        """
        return self.data < object.data
    
    def __gt__(self, object):
        """
        a method to define ">" operator
        """
        return self.data > object.data

llist = LinkedList([1, 2, 3])
# b =llist.get_element(1)
# d = llist.get_element(3)
llist.insert(1, 0)
print(llist)
print(llist.index(3))