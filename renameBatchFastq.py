#This is a script to rename multiple .fq.gz files ate once, using the name of their directories as a basis for the name
#Always be careful to check if any changes need to be done and if the code properly applies to your samples 
#(e.g in this case fq.gz files have names like FCHHWEHIWRHREHR_EUHWFUWEFU_L50_QWEHQW_[1,2]_paired.fq.gz)
#To ensure code is running as intended, run the intermediate print() steps inbetween each step
#Import the necessary libraries to select and rename file.
import pathlib
import os
import sys
import glob
import re

#Setting curent path to files
p = os.getcwd()

#Getting file list
for filepath in pathlib.Path(p).glob('*/*.fq.gz'):         #selects all .fq.gz files within the subdirectories from where the script ir run
	#oldpath = filepath.absolute()                         #confirms the absolute path to the files
	#print(oldpath)
	fpath = filepath.parent                                #captures the path up to the sample (subdirectorie where .fq.gz files are)
	#print(fpath)
	spName = filepath.parent.stem                          #captures only the name of each subdirectory
	#print(spName)
	seqName = filepath.stem                                #captures current name of each .fq.gz file
	#print(seqName)
	seqName2 =  re.sub(r'.*(_[1,2].*)', r'\1', seqName)    #in this specific case, it keeps only the _[1,2_paired.fq] part of the file name
	#print(seqName2)
	suffix = filepath.suffix                               #saves the suffix .gz as an object to append to filename later
	#print(suffix)
	new_name = f'{spName}{seqName2}{suffix}'               #creates a new file name, consisting of species/sample(subdirectory)_[1,2]_paired.fq.gz
	new_name = re.sub(r'\s+', '', new_name)                #removes any inconvinient empty space from the name
	#print(new_name)
	new_path = os.path.join(fpath, new_name)               #creates a path for the new files
	older = os.path.join(fpath, seqName + suffix)          #creates an object with the old paths and file names to feed into os.rename
	#print(older)
	#print(new_path)
	print("Move " + older + " to " + new_path)             #prints the change that's going to happen: "Move path/to/file.fq.gz to path/to/newname.fq.gz"
	#os.rename(older, new_path)                             #actually renames the files.

#Again, BEWARE OF BLINDLY RUNNING THIS SCRIPT! Always check if th print ("Move" + older + "to" + new_path) prints the wanted result before running.
#To run just delete the # before os.rename.
