#__author__ = 'Administrator'
import utilityMin
import os
import ModuleFind
import sys
#sys.setrecursionlimit(100000)

filename="hue.txt"
if os.path.exists(filename):
    os.remove(filename)

hue=utilityMin.up_sapn(0.1,5)

sort=sorted(hue.items(),key=lambda e:e[1],reverse=True)

fo=open("hue.txt","a")

for item in sort:
    fo.write('[')
    fo.write(item[0]+" : "+str(item[1]))
    fo.write(']')
    fo.write("\n")






# for key,value in hue.items():
#     fo.write('[')
#     fo.write(key+" : "+str(value))
#     fo.write(']')
#     fo.write("\n")

fo.close()

