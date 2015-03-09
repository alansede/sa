#__author__ = 'aldin'
#coding=utf-8
import os
def processDir():
    #/home/aldin/sa/softwares/tar/tar-1.20
    path="/home/aldin/sa/softwares"
    softwares=os.listdir(path)
    for software in softwares:
        pathnew=path+"/"+software
        versions=os.listdir(pathnew)
        for version in versions:
            processFile(software,pathnew+'/'+version)

            #执行程序
            execFunc(software)

def processFile(software,dir):

    #生成Makefile文件
    if not os.path.exists(dir+"/Makefile"):
        os.chdir(dir)
        os.system("./configure")
    files=os.listdir(dir)
    #修改外层Makefile
    path=dir
    changeContext(software,dir+"/Makefile")


    #修改src文件夹中的Makefile
    if "src" in files:
        path=dir+"/src"
        #修改MakeFile内容
        changeContext(software,dir+"/src/Makefile")

    #将instrument.c拷贝到源文件中
    commond="cp /home/aldin/sa/instrument.c "+path
    os.system(commond)





def changeContext(software,path):
        content=[]
        for line in open(path,"r"):
            #修改CFLAGS
            if line.startswith("CFLAGS = -g"):
                print(line)
                line="CFLAGS = -g -finstrument-functions\n"
                print(line)
            #添加instrument.c
            if line.startswith(software+"_SOURCES = "):

                str=line.split("=")
                line=str[0]+"= instrument.c "+str[1]

            if line.startswith("am_"+software+"_OBJECTS"):
                str=line.split("=")
                line=str[0]+"= instrument.$(OBJEXT) "+str[1]
            content.append(line)

        out=open(path,"w")
        for line in content:
            out.write(line);

        out.close()



def execFunc(software):
    #todo:执行各程序
    if "tar".__eq__(software):
        execTar()

    if "gzip".__eq__(software):
        execGzip()

    if "cflow".__eq__(software):
        execCflow()

def execTar():
    #todo:执行tar程序
    #每执行一次都要movefile，更改文件名
    #都要对多个/多种文件执行操作
    commond="tar -cvf test.tar "

def execGzip():
    #todo:执行gzip程序

def execCflow():
    #todo:执行cflow程序

#将数据收集到一起
def moveFile(dir):
    commond="mv functionList*.txt trace.txt graph.dot /home/aldin/sa/execOrder"
