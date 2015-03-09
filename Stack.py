#coding=utf-8
#__author__ = 'Administrator'

class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return "the stack is empty!!"

    def size(self):
        return len(self.items)