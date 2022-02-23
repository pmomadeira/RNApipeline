# Import the necessary libraries. Glob allows us to select files under diretories; os gives the
# possibility to look for file paths; re allows the use of re.compile to look for a partial string;
# csv is used to write the output as a csv file; and bs4/BeautifulSoup is the library for html parsing
import glob
import os
import re
import csv
from bs4 import BeautifulSoup

def grab_file_results(base_path):
    # Select all the html files in subdirectories. This assumes you have one large directory for the raw/trimmed 
    # files and a subdirectory for each species within that large directory.  This code looks for the fastqc.html
    # files in each of those
    fqHtmls = glob.glob("{}/*.html".format(base_path))

    # We also want to define a string to help match the files to a sample. A simple approach is to use
    # print(os.path.abspath(fqHtml), seqsF.get_text(","), file = f, sep = ','), but the os.path.abspath() funtion
    # gives us the complete path to the file. That is to large and makes it harder to read the table

    for fqHtml in fqHtmls:
        fname = open(fqHtml, 'r')
        soup = BeautifulSoup(fname.read(), 'lxml')
        seqs = soup.find(string = re.compile("Total"))
        seqsF = seqs.findparent('tr')
        sampleName = re.findall(r"{}.*/".format(base_path),fqHtml) and re.sub(r'/F.([1,2].*)', r'\1 ', fqHtml)
        print(sampleName, seqsF.get_text(","), file = f, sep = ',')

# Open and write a csv file in which the results will be written
f = open ("readCounts.csv", 'w')

algaeDict = {
    "algaeGenus" : {"Agarum", "Alaria", "Chorda", "Costaria", "Cymathaere", "Ecklonia", "Eisenia", "Egregia", "Laminaria", "Lessonia",
    "Lessoniopsis", "Macrocystis", "Nereocystis", "Pelagophycus", "Postelsia", "Pterygophora", "Saccharina", "Sachorhiza",
    "Fucus", "Ruppia", "Dictyoneurum", "Halodule", "Zostera", "Phyllospadix", "Cymodocea", "Posidonia"}, 
    "algaeCodes" : {"Ac", "Acri", "Alsp", "Am", "Asp", "Cc", "Er", "Hb", "Hn", "Lfla", "Lova","Lsae", "Lsp", "Lv", "Lyag", "MP",
    "Nl", "Sd", "S", "Ssp", "Bb", "Cf","Cm","Cr", "Da", "Fd", "Fdh", "Fdl", "Fdll", "Fdw", "Fg", "Fs", "Lq", "Mb", "Sb",
    "Sg", "Ss", "Xcho", "Xgla", "Hw", "Pi", "Rfil", "Rf", "Za", "Zj", "Zm", "Zn", "Fvir", "Pp"}
    }

for key, values in algaeDict.items():
    for entry in values:
        print("Checking if {} path exists!".format(entry))
        if os.path.exists("{}".format(entry)):
            print("Found Entry!!")
            grab_file_results(entry)
        else:
            print("Not Found!")
