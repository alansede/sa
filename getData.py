#__author__ = 'Administrator'
#coding=utf-8

import networkx as nx
import os

def getGraph():

    g=nx.DiGraph()

    #获取节点

   # for line in open("node.txt","r"):
        #print line
       # g.add_node(line)
    #加入边
    for line in open("edge.txt","r"):
        #print line
        nodes=line.strip().split(",")
        g.add_edge(nodes[0],nodes[1])
    pr=nx.pagerank(g,alpha=0.85)
    printDict(pr)
    return pr,g

def getPr():
    pr,g=getGraph()
    return pr

def printDict(dict):
    if(os.path.exists("pr.txt")):
        os.remove("pr.txt")
    out=open("pr.txt","a")
    sort=sorted(dict.items(),key=lambda e:e[1],reverse=True)
    for item in sort:
        out.write('[')
        out.write(item[0]+" : "+str(item[1]))
        out.write(']')
        out.write("\n")
    out.close()

def getSequence(file):
    sequence=[]
    for line in open(file):
        node=line.strip()
        sequence.append(node)

    return sequence


