import textract
import re
import sys

args = sys.argv

#check atleast 2 arguments are given
if len(args) < 2:
	print("Please provide job id to be tested as argument")
	sys.exit(1)
	
#get the count of the word 'the' in the entire document
def getCount():
	count=0
	try:
		text = textract.process("CERN.pdf")
		count = len(list(re.finditer(r"(\bthe\b)|(\bThe\b)", text)))
	except EnvironmentError:
		print 'Error opening file {0}'.format("CERN.pdf")
	return count

def getGangaJobCount(path):
	f = open(path, "r")
	return int((f.read()))

j=jobs[int(args[1])] #get the job with given id
answerPath=j.outputdir + "answer.txt" #get the path to the output folder
realCount = getCount()
gangaJobCount = getGangaJobCount(answerPath)

print("Real count    : " + str(realCount))
print("gangaJob count: " + str(gangaJobCount))
assert realCount == gangaJobCount, "Ganga Job's count should be" + str( RealCount)
print ("Test successful")
