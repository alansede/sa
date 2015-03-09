# __author__ = 'Administrator'
#coding=utf-8
import getData
from copy import deepcopy

exUtil = getData.getPr()
cs = getData.getSequence("functionListE.txt")
hue_set = {}
#mtd=0


def getIndex():
    index = {}
    for i in range(cs.__len__()):
        node = cs[i]
        if index.keys().__contains__(node):
            index[node].append(i)
        else:
            index[node] = [i]
    return index


index = getIndex()


def up_sapn(min_utility, mtd):
    for i in range(cs.__len__()):
        node = cs[i]
        if (ewu([node], mtd) > min_utility):
            if getUtility([node]) >= min_utility:
                # hue_set.append([node]) #将此节点加入hue_set
                hue_set[node] = getUtility([node])
            miningHUE([node], mtd, min_utility)

    return hue_set


def ewu(episode, mtd):
    ewu = 0
    #mtd=5
    #1、原来为moSet（最小时间间隔集合），但因为是有序序列，改为epSet(片段集合)
    #2、moSet还是得要，用于扩展片段
    moSet = getMoSet(episode)
    #print mo
    for mo in moSet:
        for i in range(mo[0], mo[0] + mtd):
            if i == cs.__len__():
                break
            ewu += exUtil[cs[i]]
    return ewu


def miningHUE(episode, mtd, min_utility):
    moSet = getMoSet(episode)
    for mo in moSet:
        if mo[1] + 1 >= mo[0] + mtd:
            break
        alpha = deepcopy(episode)
        for timePoint in range(mo[1] + 1, mo[0] + mtd):  # mo[start,end]
            alpha.append(cs[timePoint])  #扩展成新串
            print alpha
            if hue_set.has_key(",".join(alpha)):
                continue
            if getUtility(alpha) >= min_utility:
                #hue_set.append(alpha)
                hue_set[",".join(alpha)] = getUtility(alpha)
                #if ewu(alpha) >= min_utility:
                #   miningHUE(alpha,mtd,min_utility)


def getUtility(episode):
    utility = 0
    moSet = getMoSet(episode)
    for item in moSet:
        start = item[0]
        end = item[1]
        for i in range(start, end + 1):
            utility += exUtil[cs[i]]
    return utility


def getMoSet(episode):
    # print episode
    moSet = []
    if episode.__len__() == 1:
        return [[index[episode[0]][0], index[episode[0]][0]]]
    else:
        #return [[index[episode[0]][0], index[episode[episode.__len__() - 1]][0]]]

        pos = index[episode[0]]
        for ind in pos:
            if subList(cs, ind, ind + (episode.__len__())) == episode:
                moSet.append([ind, (ind + episode.__len__())])

        return moSet

def subList(list,start,end):
    sub=[]
    for i in range(start,end):
        if i<list.__len__():
            sub.append(list[i])

    return sub




