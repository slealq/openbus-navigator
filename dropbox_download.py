#!/usr/bin/python

"""
Communicates to dropbox, and downloads the .csv file that should be in the root folder of dropbox. 
"""

# Defining the libraries used in this file.
import dropbox, os, sys, file_manipulation, directory_manipulation

# Beginning of the main file function.
try:
    access_token=open("access_token", "rw+")# Get the access code from the file access_code
except IOError:
    print "There's no access_token file in your directory. Try running request_acces first."
    sys.exit()
client = dropbox.client.DropboxClient(access_token.next())# Get the client response used for manipulation.
try:# Try to search files in dropbox
    files_gpx = client.search('/','.gpx')
    if files_gpx==[]:
        print "I haven't found any .gpx in your dropbox..."
        sys.exit()
    else:
        print "I have found the following .gpx in your dropbox: "
        for file in files_gpx:
            print "\t",file.get('path')
        answer=raw_input("Do you wish to download them all to RAW directory? (Y/n): ")
        if answer=="Y":
            directory_manipulation.ensure_dir('RAW')# Create directory
            os.chdir('RAW')# Change directory to RAW
            for file in files_gpx:# For each file in files_gpx do the following
                target_gpx=client.get_file(file.get('path'))# Get the file object
                file_manipulation.write_or_overwrite(file.get('path').rpartition("/")[2], target_gpx.read())# Write the file 
        elif answer=="n":
            print "Exiting now..."
            sys.exit()
        else:
            print "Not suitable option, exiting now..."
            sys.exit()
except NameError:
    print "There was an error, please check if everything is running well."
