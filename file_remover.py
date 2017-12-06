#simple python script for deleting files
import os
import sys
filename = raw_input("Enter filename : ")
for files in os.listdir("."):
	if filename == files:
		if raw_input("Are you sure to delete this file [y/n] : ") == "y":
			try:
				os.remove(filename)
				sys.exit(0)
			#sys.exit() raises an exception, called  SystemExit
			except SystemExit:
				print "successfully removed :) "
				sys.exit(0)
			except:
				print "error ! "
print "File Not Found!"
