#/usr/share/python

"""
This file will contain some methods for creating data from a gpx file and creating a gpx file from data. In a future this will substitude the way we create txt files, with the file_manipulation and gpx_parser scripts. Instead this script will use gpxpy, for making the function cleaner.
"""

# Libraries
import gpxpy
import gpxpy.gpx
import file_manipulation as fm # Custom library
import directory_manipulation as dm # Custom library
import os

# Variables

# Helpers
def gpx2data():
    """ This should return in some way the data of the gpx file. """
    pass

def data2gpx(lat_and_lon):
    """ This will return a gpx file for posterior writing in disk, from data """
    gpx_file= gpxpy.gpx.GPX()
    
    # Create first track of the new gpx file
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx_file.tracks.append(gpx_track)

    # Create first segment of the track
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    # gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234, 5.1234, elevation=1234)) THIS IS THE WAY TO ADD POINTS
    for items in range(0, len(lat_and_lon)):
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat_and_lon[items][0], lat_and_lon[items][1], elevation=0))#elevation is not calculated by find_stops

    # Now writes the new GPX file into a directory called GPX, that has the results of the find_stops algorithm
    dm.ensure_dir("GPX")
    os.chdir(os.getcwd()+'/GPX')
    fm.write_or_overwrite("paradas.gpx", gpx_file.to_xml())

# Methods


