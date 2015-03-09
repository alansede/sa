#__author__ = 'Administrator'
#coding=utf-8

import Stack
import getData
import os

def findModule():
    modules=[]
    es=getData.getSequence("functionListBigFile.txt")
    mainFun=es[0][1:]
    stack=Stack.Stack()
    #used to store the module
    seq=[]
    stack.push(mainFun)
    for i in range(1,len(es)):
        node=es[i]
        if node.startswith('E'):
            stack.push(node[1:])
            seq.append(node[1:])

        elif node.startswith('X'):
            stack.pop()
            if mainFun.__eq__(stack.top()):
                modules.append(seq)
                seq=[]

    return modules

def printMo():

    modules=findModule()

    if os.path.exists("modules.txt"):
        os.remove("modules.txt")
    fo=open("modules.txt",'w')
    for module in modules:
        fo.write(",".join(module))
        fo.write("\n")

    fo.close()







