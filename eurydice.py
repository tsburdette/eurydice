# required libraries
import socket
import time
import sys

# constants
true    = 1

# Bot vars
server  = "irc.rizon.net"
port    = 6667
channel = "#orpheus"
nick    = "Eurydice"
pword   = "lyric"

def ping ():
    sock.send (b"PONG : ping\n")

def sendmsg (chan, msg):
    sock.send(("PRIVMSG " + chan + " :" + msg + "\n").encode())

def joinchan (chan, password):
    sock.send(bytes("JOIN %s %s\r\n" % (chan, password), "UTF-8"))
    
def sendnick (nick):
    sock.send(bytes("NICK %s\r\n" % nick,"UTF-8"))
    
def sendpass (password):
    sock.send(bytes("PRIVMSG NickServ IDENTIFY %s\r\n" % password, "UTF-8"))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))

sock.send(bytes("NICK %s\r\n" % nick, "UTF-8"))
sock.send(bytes("USER %s %s bla : %s\r\n" % (nick, server, nick), "UTF-8"))
sock.send(bytes("JOIN #orphtest\r\n", "UTF-8"))
sendmsg("#orphtest", "Hello! I am a bot!")

readbuffer = ""

while true:
    #time.sleep(5)
    readbuffer = sock.recv(1024).decode("UTF-8")
    print(readbuffer)
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()
    
    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)
        
        if(line[0] == "PING"):
            sock.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
        for index, i in enumerate(line):
            #print(*line)
            if(".quit" in line[index]):
                print("Found quit command at %s" % index)
                sys.exit()
