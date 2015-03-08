def execTar(version):
	commond="\
			cp ~/sa/file1 ~/sa/file2  . ;\
			./tar -c test.tar file1 file2\
			pvtrace ./tar"
	os.system(commond)

	moveFile(version)
			



'''

cp ~/sa/file1 ~/sa/file2 .

./tar -c test.tar file1 file2

pvtrace ./tar

'''

****************************************************

def execGzip(version):
	commond="cp ~/sa/file1 . ; ./gzip file1 ; pvtrace ./gzip"
	os.system(commond)

	moveFile(version)

	'''cp ~/sa/file1 .
	./gzip file1
	pvtrace ./gzip'''





def execCflow(version):
	commond="./cflow main.c ; pvtrace ./cflow"
	os.system(commond)

	moveFile(version)


	
def moveFile(version):
	commond="\
		mv funcListE ./sa/execOrder/"funcListE_"+version ;\
		mv funcListEX ./sa/execOrder/"funcListEX_"+version;\
		mv funcListSys ./sa/execOrder/"funcListSys_"+version;\
		mv trace.txt ./sa/execOrder/trace.txt;\
		mv graph.dot ./sa/execOrder/graph.dot"
	os.system(commond)