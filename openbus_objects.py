#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Programm that takes .txt files with GPS waypoints inside and creates 
objects of Class stops
'''    
class GpsTrack:
    '''
    Atributes:
    ID := (Int) has the identifier of each track
    _name := (str) has the original file name of track
    _date := (str) has the date of file creation in format YYYY/MM/DD/hh/mm
    waypoints := (list) has an internal lists of information of every gps point
    on track format [latitud,longitude,elevation,time]
    '''
    ID=0
    _name=""
    _date=""
    waypoints=[]
    
    #Builder
    def __init__(self, path, ID):
        self.ID=ID
        if path!="" and path[path.find("."):]==".txt":
            file=open(path, "r")
            waypoints=[]
            for line in file:
                if line.startswith("<name>"):
                    self._name=sub_string("<name>","</name>",line)
                    self._date=sub_string("Track ","</name>",line)
                elif line.startswith("<trkpt"):
                    lat=float(sub_string('lat="','" lon',line))
                    lon=float(sub_string('lon="','">\n',line))
                    ele=float(sub_string('<ele>','</ele>',file.readline()))
                    time=sub_string('<time>','</time>',file.readline())
                    waypoints.append([lat,lon,ele,time])
            file.close()
            self.waypoints=waypoints
