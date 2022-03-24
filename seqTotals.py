#Import the necessary libraries. Glob allows us to select files under diretories; os gives the
#possibility to look for file paths; re allows the use of re.compile to look for a partial string;
#csv is used to write the output as a csv file; and bs4/BeautifulSoup is the library for html parsing
import glob
import os
import re
import csv
from bs4 import BeautifulSoup

#Open and write a csv file in which the results will be written
f = open ("readCounts.csv", 'w')

#Select all the html files in subdirectories. This assumes you have one large directory for the raw/trimmed 
#files and a subdirectory for each species within that large directory.  This code looks for the fastqc.html
#files in each of those
fqHtmls = glob.glob("*/*.html")

#We also want to define a string to help match the files to a sample. A simple approach is to use
#print(os.path.abspath(fqHtml), seqsF.get_text(","), file = f, sep = ','), but the os.path.abspath() funtion
#gives us the complete path to the file. That is to large and makes it harder to read the table

for fqHtml in fqHtmls:
	base_path = os.getcwd().rsplit('/', 2)[1]
	print(base_path)
	fname = open(fqHtml, 'r')
	soup = BeautifulSoup(fname.read(), 'lxml')
	seqs = soup.find('td', string = "Total Sequences")
	seqsF = seqs.find_parent('tr')
	sampleName = re.findall(r"{}.*/".format(base_path),fqHtml) and re.sub(r'/.*(_[1,2].*)', r'\1 ', fqHtml)
	print(sampleName, seqsF.get_text(","), file = f, sep = ',')
