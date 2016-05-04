#!/usr/bin/python

"""
Here it will go a helper function that will find the bus stops according to a custom algorithm suggested by Federico Ruiz.
"""

# Libraries
import os, re
from geopy.distance import great_circle

# Variables
PATH=os.getcwd()+'/'+'TXT'# This makes the assumption that we are working in a parent directory, where there is a directory named TXT
PHI=120# Quantity in meters for the tolerance in the search in m

# Helper functions
def bus_stops(txt_files_names):
    """This method calculates the bus stop points according to the points where the number of routes that are availabe change. It's input is the txt files that are in TXT."""

    # Variables
    lat_lon=[]#Variable for saving the names of the file that i have already used so that i dont repeate values.
    neighboors=''#String for the moment

    for name in txt_files_names:# For each file that it has as input
        txt_contents=open(PATH+'/'+name, 'r').read()# Reads the content in each 
        for line in txt_contents.split('\n'):# For each line in that file
            if not re.match(r"[0-9e \t+.-]*$", line):# If line contains something
                lat_lon.append((line.split(' ')[0], line.split(' ')[1]))
                # This last step updates a list with two values that are separated by a space, the first two.

    for i, entry in enumerate(lat_lon):# For each item! 
        print (i, entry)
        for rest_entries in range(0, len(lat_lon)):# For the items after that
            print great_circle(entry, lat_lon[rest_entries]).m
            if great_circle(entry, lat_lon[rest_entries]).m<=PHI:
                neighboors+="Point number "+str(i)+" and "+str(rest_entries)+" are neighboors\n"
    print neighboors

    print str(lat_lon[210])+" "+str(lat_lon[193])
# Main start
bus_stops(os.listdir(PATH))
