#!/usr/bin/env python

'''
Programm that takes .txt files with GPS waypoints inside and creates 
objects of Class GpsTracks.
'''

# Last Changes: Fix path() search for .txt

from datetime import datetime
from os import listdir

def sub_string(str_in, str_end, string):
    '''
    Function that creates a subString from the final index of strIni until
    the first inde of strFin taking a copy of the inicial string. Parameters:
    str_in := (str) first index
    str_end := (str) end index
    string := (str) initial string
    Return sub_str := (str) of return.
    Exception: If no coincidence between strIni and strFin on string returns
    None
    ''' 
    if str_in in string and str_end in string:
        index_ini = string.find(str_in)+len(str_ini)
        index_end = string.find(str_end)
        sub_str = string[index_ini:index_end]
    else:
        sub_str = None
    return sub_str

def lista_lat_lon(track):
    '''
    Function that returns a list of tuples which contains latitudes and
    longitudes. Takes as parameter a GpsTrack object.
    track := (GpsTrack) where waypoint are taken
    Returns lists := (list) of tuples with fromat (lat,lon) 
    '''
    lists = []
    if type(track) is GpsTrack: 
        for i in Track.waypoints():
            lists.append((i[0],i[1]))       
    else:
        print ("Error 0X01: The DataType enter is not a GpsTrack") 
    return lists
    
def common_diff_WayPoints(Tracks):
    '''
    Function that compares latitude and longitude of the differents objets in a Track list, and returns common waypoints within a error margen and a list of waypoints that differ from the common
    Tracks := Object list of  GpsTrack 
    Return waypointsCom := list of common waypoints in the format [lat, lon]'''
     
    waypointsList = [] #list of waypoints obtain from the Track received
    waypointsCom = []  #common waypoints list
    waypointsDif = []  #waypoints that differ from the common waypoints
    
    for i in Tracks:
        waypointsList.append(listaLatLon(i)) #get latitude and longitude of each waypoint

    sorted(waypointsList, key=len) #order from smallest to biggest waypoint list

    n = len(waypointsList)
    #Find a temporary route by waypoints list, taking the biggest list of waypoints as reference
    temp1 = [[]]*len(waypointsList[n])
    for i in range(0,len(waypointsList[n]))
        newStandar = waypointsList[n][i][0]
        for entry in range(0,len(waypointsList))
            for j in range(0,len(waypointsList[entry])
                if waypointsList[entry][j][0] in range(newStandar-newStandar*0.00005,newStandar+newStandar*0.00005,)
                    temp1[i].append(waypointsList[entry][j])
    #Change the to waypointsDif the temp1[position] that has only one element
    for data in range(0,len(temp1))
        for i in range(0,len(temp1[data]))
            if len(temp1[data][i])==1
            waypointsDif.append(i)
            del temp1[data][i]
    #Check if all the data of each waypoint is on the temp1 list, if not it is change to waypointsDif
    for data in range(0,len(temp1))
            for position in range(0,len(temp1[data])
                    if waypointsList[data][position] not in temp1
                    waypointsDif.append(waypointsList[data][j])
            
    #Remove all empty spaces from temp1    
    temp2 = filter(None,temp1)

    #Final common waypointsList,as an average of the similar (lat,lon) data
    latTemp = 0
    latTemp = 0
    for i in range(0,len(temp1))
        for j in range(0,len(temp1[i]))
           latTemp = temp1[i][j][0] + latTemp
           lonTemp = temp1[i][j][1] + lonTemp
        latitude = latTemp/len(temp1[i])
        longitude = lonTemp/len(temp1[i])
        waypointsCom.append([latitude,longitude])

    return waypointsCom,waypoinstDif 
        
    
class GpsTrack:
    '''
    Atributes:
    ID := (Int) has the identifier of each track
    _name := (str) has the original file name of track
    _date := (str) has the date of file creation in format YYYY/MM/DD/hh/mm
    waypoints := (list) has an internal lists of information of every gps point
    on track format [latitud,longitude,elevation,time]
    '''
    ID = 0
    _name = ""
    _date = ""
    waypoints = []
    
    #Builder
    def __init__(self, path, ID):
        self.ID = ID
        if path != "" and path[path.find("."):] == ".txt":
            file = open(path, "r")
            waypoints = []
            cont = 0
            for line in file:
                if line.startswith("<name>"):
                    self.name = subString("<name>","</name>",line)
                    self.date = subString("Track ","</name>",line)
                elif line.startswith("<trkpt"):
                    lat = float(subString('lat="','" lon',line))
                    lon = float(subString('lon="','">\n',line))
                    ele = float(subString('<ele>','</ele>',file.readline()))
                    time = subString('<time>','</time>',file.readline())
                    waypoints.append([lat,lon,ele,time])
            file.close()
            self.waypoints = waypoints

    
def main():
    # List of GpsTrack objects
    tracks = []
    cont = 1
    for i in listdir("./TXT"): #Add where the file TXT is,where it is locate the data for reading
        if i[i.find("."):] == ".txt":
            tracks.append(GpsTrack("./TXT"+i,cont))
            cont+=1            
    for i in tracks:
        print (i.ID) #Screen print for good working
    print "The estimated route for this input data is "     
main() #Run the main
