#!/usr/bin/python

"""
Here it will go a helper function that will find the bus stops according to a custom algorithm suggested by Federico Ruiz.
"""

# Libraries
import os, re
from geopy.distance import great_circle

# Variables
PATH=os.getcwd()+'/'+'TXT'# This makes the assumption that we are working in a parent directory, where there is a directory named TXT
PHI=15# Quantity in meters for the tolerance in the search in m

# Helper functions
def bus_stops(txt_files_names):
    """This method calculates the bus stop points according to the points where the number of routes that are availabe change. It's input is the txt files that are in TXT."""

    # Variables
    lat_lon=[]#Variable for saving the names of the file that i have already used so that i dont repeate values.
    neighboors=[]#Array of arrays. The first contains neighboors and the second list of neighboors.
    flag_first=flag_second=False# Flags for neighboors finding algoritm
    
    for name in txt_files_names:# For each file that it has as input
        txt_contents=open(PATH+'/'+name, 'r').read()# Reads the content in each 
        for line in txt_contents.split('\n'):# For each line in that file
            if not re.match(r"[0-9e \t+.-]*$", line):# If line contains something
                lat_lon.append((line.split(' ')[0], line.split(' ')[1]))# Add first two items to a list of items.

    for i, entry in enumerate(lat_lon):# For each item! 
        for rest_entries in range(i+1, len(lat_lon)):# For the items after that
            if great_circle(entry, lat_lon[rest_entries]).m<=PHI:# If distance between two points is less tha PHI
                for item_list in range(0, len(neighboors)):# Compare for all list item in neighboors
                    for item in range(0, len(neighboors[item_list])):# Compare for all items in each list.
                        if neighboors[item_list][item]==entry:# If the first value is already in a list: 
                            flag_first=True# Raise a flag about it
                            item2add=lat_lon[rest_entries]# Save the item opposite to the one already in the list.
                            list_point=item_list# Save the list in which the item was founded
                        elif neighboors[item_list][item]==lat_lon[rest_entries]:#lat_lon[rest_entries]:# If the second termin is founded: 
                            flag_second=True# Raise a flag about it
                            item2add=entry# Same as above...
                            list_point=item_list
                if flag_first and flag_second:# Now, if both flags were raised: 
                    flag_first=flag_second=False# It means it is the reciproque of what it was founded before.
                elif flag_first and not flag_second:# If only the first flag was raised: 
                    neighboors[list_point].append(item2add)# Add the other item in the list pos.
                    flag_first=False# Set the flag to false again
                elif not flag_first and flag_second:# If the second flag was raised: 
                    neighboors[list_point].append(item2add)# Add the other item (first item) to the corresponding list.
                    flag_second=False# Set the flag to false again
                else:# If the founded items are not in any list, then: 
                    neighboors.append([entry, lat_lon[rest_entries]])# Make a new list with both items.
                
    for item_list in range(0, len(neighboors)):
        print neighboors[item_list]
            
    #print str(lat_lon[210])+" "+str(lat_lon[193])
# Main start
bus_stops(os.listdir(PATH))
