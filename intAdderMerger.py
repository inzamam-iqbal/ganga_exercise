import os
def mergefiles(file_list,output_file):
	outFile = file(output_file,'w')
	tot=0
	for f in file_list:
		tempFile = file(f)
		tot=tot+int(tempFile.read())
		tempFile.close()
	outFile.write(str(tot))
	outFile.flush()
	outFile.close()
	return True
