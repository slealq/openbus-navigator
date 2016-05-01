#!/usr/bin/python

"""
Contains a little script that grabs ALL the files in RAW and converts them to txt in a folder named TXT.
"""

# Defining the libraries used in this file.
import os, file_manipulation, directory_manipulation, sys

# Helper functions

# Main start
PATH=os.getcwd()+'/'+'RAW'# Creates the path to the RAW directory
if os.path.exists(PATH):
    print "I have found an existing RAW directory. Going to convert GPX files that are in there."
elif not os.path.exists(PATH):
    print "Haven't found any RAW directory. Try running dropbox_download first."
    sys.exit()# Exits the program

directory_manipulation.ensure_dir('TXT')# Ensures the TXT directory exists
os.chdir(os.getcwd()+'/TXT')

for file in os.listdir(PATH):
    print "\tConverting",file
    gpx_file=open(PATH+'/'+file, 'rw+')# Opens the file
    file_manipulation.write_or_overwrite(file.rpartition('.')[0]+'.txt', file_manipulation.gpx_to_txt(gpx_file))
print "Finished parsing. Exiting now."
