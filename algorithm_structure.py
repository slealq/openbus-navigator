#!/usr/bin/env python

'''
Programm that takes .txt files with GPS waypoints inside and creates 
objects of Class GpsTracks.
'''

# Last Changes: Fix path() search for .txt

from datetime import datetime
import os

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
        index_in=string.find(str_in)+len(str_in)
        index_end=string.find(str_end)
        sub_str=string[index_in:index_end]
    else:
        sub_str=None
    return sub_str

def lista_lat_lon(track):
    '''
    Function that returns a list of tuples which contains latitudes and
    longitudes. Takes as parameter a GpsTrack object.
    track := (GpsTrack) where waypoint are taken
    Returns lists := (list) of tuples with fromat (lat,lon) 
    '''
    lists=[]
    if type(track) is GpsTrack: 
        for i in Track.waypoints():
            lists.append((i[0],i[1]))       
    else:
        print ("Error 0X01: The DataType enter is not a GpsTrack") 
    return lists

'''Rutas CODIGO EN PROCESO NO ESTA LISTO    
def commonWayPoints(Tracks, epsilon, porc):
    
    Función que compara las latitudes y longitudes de todos los waypoints de un track
    y genera un listado común. Tomando un rango de error (epsilon) entre los datos
    Parametros:

    Tracks := Lista de objetos GpsTrack 
    epsilon := float que indica el rango de error en los datos
    porc := int que indica el porcentaje en común que deben tener los waypoints 
    Return waypointsCom := listado de waypoints en común en formato [lat, lon]
     
    listaRutas = []
    for i in Tracks:
        listaRutas.append(listaLatLon(i))
    for j in listaRutas[0]:
        
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

    
def main():
    # List of GpsTrack objects
    PATH=os.getcwd()+'/'+'TXT'
    tracks=[]
    cont=1
    for i in os.listdir(PATH): 
        if i[i.find("."):]==".txt":
            tracks.append(GpsTrack(PATH+'/'+i,cont))
            cont+=1            
    for i in tracks:
        print (i.ID) #Screen print for good working
        
main() #Run the main
