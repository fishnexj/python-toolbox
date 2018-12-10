#utility functions for working with REST APIs

def write2File(data,fileName):
# write data from an API response to a file
	from sys import stdout
	output = stdout #saves sys.stout as blank (i.e. our normal setting)
	fh = open(fileName, "w") #create the file we will write to
	stdout = fh #assign standard output to this file
	print(data) #anything I print here will go into the file
	stdout = output #resets the standard output so future prints don't go into the file
	fh.close() #we're all done with the file, so let's close it

def apiLog(url,message):
# print the URL and whether calling it worked...
	statusDataVersion = str( url ) + "," + str( message )
	statusPrintVersion = str( url ) + " --- " + str( message )
	print( statusPrintVersion)
