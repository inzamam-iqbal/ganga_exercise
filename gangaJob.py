from PyPDF2 import PdfFileReader, PdfFileWriter
import os

args=[]
splitFolder="pages"
#split the pdf and save each page as a pdf in splitFolder folder
def splitPdf(path):
	inputpdf = PdfFileReader(open(path, "rb"))
	if not os.path.exists(splitFolder):
		os.makedirs(splitFolder)
	for i in range(inputpdf.numPages):
		output = PdfFileWriter()
		output.addPage(inputpdf.getPage(i))
		with open("%s/page%s.pdf" % (splitFolder, i),"wb") as outputStream:
		    output.write(outputStream)
		    args.append(["page%s.pdf" % i]) #append each file name as a list to args

#get all the files in the splitFolder folder as a list of LocalFile
def getFiles():
	files=[]
	for filename in os.listdir(splitFolder):
		files.append(LocalFile(str(os.path.join(splitFolder, filename))))
	return files
		
splitPdf("CERN.pdf")

j=Job(name='Ex1')
j.application.exe = File('theCounter.py')
j.inputfiles = getFiles()
j.splitter=ArgSplitter(args=args)
j.outputfiles = [ LocalFile('answer.txt') ]
j.postprocessors=CustomMerger(files=['answer.txt'],module=File('intAdderMerger.py'))
j.submit()
while (j.status != 'completed'):
	pass
