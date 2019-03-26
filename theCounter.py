#!/usr/bin/env python

import sys
import textract
import re

args = sys.argv
#check atleast 2 arguments are given
if len(args) < 2:
	print("Please provide a file path as argument")
	sys.exit(1)

filePath = args[1]
count=0
try:
	text = textract.process(filePath)#extract the text from pdf
	count = len(list(re.finditer(r"(\bthe\b)|(\bThe\b)", text)))#count the word 'the' and 'The'
except EnvironmentError:
	print 'Error opening file {0}'.format(filePath)
outFile=open('answer.txt','w')
outFile.write(str(count))
