#!./venv/bin/python

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 21 Jan 2024
# Date Modified : -
# Description   :  
# Usage         : stack.py
#####   #####   #####

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        if self.height == 0:
            return None
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return True
    
    def push_stack(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop_stack(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    def bottom_stack(self):
        if self.height == 0:
            return None
        temp = self.top
        while self.top.next is not None:
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            print(f'self.height: {self.height}')
            temp = self.top
        return temp