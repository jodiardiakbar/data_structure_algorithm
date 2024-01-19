#!/usr/bin/python3

#####   #####   #####
# Author        : Jodiardi Akbar
# Date Created  : 18 Jan 2024
# Date Modified : -
# Description   : singly linked list class
# Usage         : singly_linked_list.py
#####   #####   #####

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Singly_LL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return True
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop_node(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail= pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first_node(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_node(self, index, value):
        temp = self.get_node(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend_node(value)
        if index == self.length:
            return self.append_node(value)
        new_node = Node(value)
        temp = self.get_node(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first_node()
        if index == self.length:
            return self.pop_node()
        prev = self.get_node(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse_node(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after