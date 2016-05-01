"""
Helper function to create a given directory or don't if already exists
"""

#Defining the libraries used in this file.
import os

# Helper function
def ensure_dir(directory_name):
    """Makes sure the directory exists, or creates it if doesn't."""
    directory_path = os.getcwd()+'/'+directory_name # Create the directory path
    if not os.path.exists(directory_path):#If it doesn't exists, create it.
        os.mkdir(directory_name, 0755)
        print "Created directory",directory_name,"in",directory_path,"succesfully"
       
