from PyPDF2 import PdfFileReader, PdfFileWriter
import os

args=[]
#split the pdf and save each page as a pdf in 'doc' folder
def splitPdf(path):
	inputpdf = PdfFileReader(open(path, "rb"))
	if not os.path.exists('doc'):
		os.makedirs('doc')
	for i in range(inputpdf.numPages):
		output = PdfFileWriter()
		output.addPage(inputpdf.getPage(i))
		with open("doc/page%s.pdf" % i, "wb") as outputStream:
		    output.write(outputStream)
		    args.append(["page%s.pdf" % i]) #append each file name as a list to args

#get all the files in the 'doc' folder as a list of LocalFile
def getFiles():
	files=[]
	for filename in os.listdir("doc"):
		files.append(LocalFile(str(os.path.join("doc", filename))))
	return files
		
splitPdf("CERN.pdf")

j=Job(name='Ex1')
j.application.exe = File('theCounter.py')
j.inputfiles = getFiles()
j.splitter=ArgSplitter(args=args)
j.outputfiles = [ LocalFile('answer.txt') ]
j.postprocessors=CustomMerger(files=['answer.txt'],module=File('intAdderMerger.py'))
j.submit()

