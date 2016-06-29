#Server class

#! /usr/bin/env python

import socket, sys, os, directory_manipulation,file_manipulation, glob

#Declaration of host and port in which the client will connect
host = 'localhost'
port = 8000
address = (host, port)

#Creation of the socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

#waiting for incoming data
print "Listening for client . . ."
conn, address = server_socket.accept()

print "Connected to client at ", address
#The server first receives the type of connection that the client requires


while True:
    #instruction = raw_input()
    msg = conn.recv(2048)
    data = []
    data = msg.split('<>')
    instruction = data[0]
    
    #if the client doesnt wish to communicate anymore the connection is closed 
    if instruction.strip() == "disconnect":
        conn.send("Chao cliente")
        conn.close()
        sys.exit("Received disconnect message.  Shutting down.")

    #if the client wishes just the bus stops information it is send....
    if instruction.strip()=="map":
        conn.send("Ya le mando los waypoints")

        #first by opening the directory of its location...
        os.chdir("GPX")

        #and then sending each one of it line by line 
        for filename in glob.glob("*.gpx"):
            f = open(filename,'r')
            l = f.read(1024)
            while (l):
                conn.send(l)
                print('Sent ',repr(l))
                l = f.read(1024)
            f.close()
    #if the intruction is anything else the server will receive the data coming from the user
    elif instruction:
        #Here it receives it
        
        print "Message received from client"

        directory_manipulation.ensure_dir('RAW')# Create directory for the data
        os.chdir('RAW')# Change directory to RAW
        #and opens a file in which the data will be saved
        with open('received_file', 'wb') as f:
            print 'file opened'
            #while True:
            for file in data:
                print file
                f.write(file)# write data to a file
            if not data:
                break
            
        
