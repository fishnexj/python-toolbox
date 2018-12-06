import sys

def io(data,fileName):
	output = sys.stdout #saves sys.stout as blank (i.e. our normal setting)
	fh = open(fileName, "w") #create the file we will write to
	sys.stdout = fh #assign standard output to this file
	print(data) #anything I print here will go into the file
	sys.stdout = output #resets the standard output so future prints don't go into the file
	fh.close() #we're all done with the file, so let's close it
