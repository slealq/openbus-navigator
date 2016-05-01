#!/usr/bin/env python

'''
    Programa que toma archivos .txt con los tracks GPS y los descompone en
    objetos de la Clase GpsTracks.
    Últimos cambios agregar la función main() con la creación de lista de tracks
'''

from datetime import datetime
from os import listdir



def subString(strIni, strFin, string):
    '''
    Funcion que genera un subString después de un strIni hasta un strFin tomando
    como padre a string. Retorna el substring formado entre ambos parametros
    
    strIni := str inicial
    strFin := str final
    string := str de origen
    Return subStr := str de retorno y -1 en caso de que no exista coincidencia
    ''' 
    if strIni in string and strFin in string:
        indexIni = string.find(strIni)+len(strIni)
        indexFin = string.find(strFin)
        subStr = string[indexIni:indexFin]
    else:
        subStr = -1
    return subStr

def listaLatLon(Track):
    '''
    Función que devuelve una lista de tuplas con las latitudes y longitudes en
    el objeto Track pasado por parametro.
    Parametro:
    Track := GpsTrack del que se toamaran los waypoints
    Return lista := listado de tuplas de la forma (lat,lon) 
    '''
    lista = []
    if type(Track) is GpsTrack:
        for i in Track.waypoints():
            lista.append((i[0],i[1]))       
    else:
        print ("Error 0X01: El tipo de dato ingresado no es GpsTrack") 
    return lista

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
        Atributos:
        ID = Integer que contiene el identificador del track
        name = string que posee el nombre del archivo del track
        date = string que posee la fecha de creacion del track en formato
    AAAA/MM/DD/hh/mm
        waypoints = array de listas que contiene la informacion de todos los
    puntos gps tomados en el track en formato [lat,lon,ele,time]
    '''
    ID = 0
    name = ""
    date = ""
    waypoints = []
    
    #Constructor por defecto de la clase
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
    # Creación de una lista de objetos GpsTracks
    tracks = []
    cont = 1
    for i in listdir("."):
        if i[i.find("."):] == ".txt":
            tracks.append(GpsTrack(i,cont))
            cont+=1            
    for i in tracks:
        print (i.ID) #Prueba de creación de los objetos GpsTracks

    #Acá empieza el algoritmo para Ruta y para Paradas
        
main()
