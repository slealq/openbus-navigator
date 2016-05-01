

"""
This file contains a set of functions that enable the user to manipulate files in a correct way. 
"""

# Defining the libraries used in this file.
import os

# Helper functions
def write_or_overwrite(name_of_file, file_contents):
    """This is the helper function that checks if the file exists and overwrites it, if it doesn't creates a new one"""
    try:# Try to open the file, if it does set a flag about it.
        file=open(name_of_file, "rw+")
        file_existed=True
        print "There's already a "+name_of_file+" file!"
    except IOError:# If it throw an error, then set a flag about it.
        file_existed=False

    if file_existed:
        # If this flag is set to true, the overwrite the file.
        print "Replacing existing file "+name_of_file+" ..."
        file.write(file_contents)
        file.close()# Close the file.

    else:
        # If the file doesn't exists, then create it.
        print "Creating new file "+name_of_file+" ..."
        file=open(name_of_file, "a")# Open the file differently. This creates the file if it doesn't exists.
        file.write(file_contents)
        file.close()# Close the file.

def string_cutter(string, init_char, final_char, init_pos_value, method_type):
    """Returns the string part between the two substrings given"""
    temp_argument=''

    if method_type==0:# If the method_type is one (used for the track_points), the don't erase the beginning tab
        init_pos=string.find(init_char, init_pos_value)# Gets the init pos of the track points information in the string
        final_pos=string.find(final_char, init_pos)# Gets the final pos of the track points information in the given string
        for pos in range(0, (final_pos-init_pos)):# For each single char in the middle of those positions, make a string about it
            temp_argument+=string[init_pos+pos]
        return [temp_argument, final_pos]# Return the string

    elif method_type==1:# Similar to the method above, only diferrence is that this DOES eliminates the initial_char that user searched
        init_pos=string.find(init_char, init_pos_value)+len(init_char)# Here you can see that it adds the length of the char to the initial pos
        final_pos=string.find(final_char, init_pos+1) # From here everything is the same
        for pos in range(0, (final_pos-init_pos)):
            temp_argument+=string[init_pos+pos]
        if string.find(init_char)==-1:
            print 'Theres no',init_char,"in one of the lines. Giving it a null value"
            temp_argument="null"
            final_pos=init_pos
        return [temp_argument, final_pos]

    else:
        return [0,0]# Maybe if the user gives a wrong method information.
        
def gpx_to_txt(gpx_file_name):
    """This helper function does a easy parsing method and creates a line with the information about each point separated by a space"""

    # Variables
    gpx_file=gpx_file_name.read()
    position=0
    txt_file=''
    
    # Starts the parsing
    while string_cutter(gpx_file, "<trkpt", "</trkpt>", position, 0)[0]!='':# While it encounters a new track point
        trkpoint=string_cutter(gpx_file, "<trkpt", "</trkpt>", position, 0)# Creates list trkpoint that contains the string and the final value position.
        latitude=string_cutter(trkpoint[0], '"', '"', 0, 1)# Gets the value of important data for each trackpoint
        longitude=string_cutter(trkpoint[0], '"', '"', latitude[1]+1, 1)
        elevation=string_cutter(trkpoint[0], '<ele>', '</ele>', longitude[1], 1)
        time=string_cutter(trkpoint[0], '<time>', '</time>', elevation[1], 1)
        speed=string_cutter(trkpoint[0], '<gpx10:speed>', '</gpx10:speed>', time[1], 1)
        accuracy=string_cutter(trkpoint[0], '<ogt10:accuracy>', '</ogt10:accuracy>', speed[1], 1)
        course=string_cutter(trkpoint[0], '<gpx10:course>', '</gpx10:course>', speed[1], 1)
        line=latitude[0]+" "+longitude[0]+" "+elevation[0]+" "+time[0]+" "+speed[0]+" "+accuracy[0]+" "+course[0]+"\n"# Writes ti all to a new line
        txt_file+=line# Adds the new line to the output
        position=trkpoint[1]# Gets the final pos and writes it as a new position
    return txt_file
