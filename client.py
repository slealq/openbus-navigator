import socket, os ,glob                   # Import socket module

s = socket.socket()             # Create a socket object
host = 'localhost'     # Get local machine name
port = 8000                    # Reserve a port for your service.

s.connect((host, port))

os.chdir("GPX")
for filename in glob.glob("*.gpx"):
    f = open(filename,'r')
    l = f.read(1024)
    while (l):
        s.send(l)
        print('Sent ',repr(l))
        l = f.read(1024)
    f.close()

print('Successfully send the file')

s.send("map")
print('connection closed')
