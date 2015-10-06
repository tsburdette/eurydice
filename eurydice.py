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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))

def ping (key):
    sock.send("PONG : " + key + "\r\n")

def sendmsg (chan, msg):
    sock.send("PRIVMSG " + chan + " :" + msg + "\r\n")

def joinchan (chan, password):
    sock.send("JOIN " + chan + " " + password + "\r\n")

def senduser ():
    sock.send("USER %s %s bla :%s\r\n" % (nick, server, nick))
    
def sendnick ():
    sock.send("NICK " + nick + "\r\n")
    
def sendpass (password):
    sock.send("PRIVMSG NickServ IDENTIFY " + password + "\r\n")




senduser()
sendnick()
sendpass(pword)
sock.send("JOIN #orphtest\r\n")
sendmsg("#orphtest", "Hello! I am a bot!")

readbuffer = ""

while true:
    readbuffer = sock.recv(1024)
    print(readbuffer)
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()
    
    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)
        
        if(line[0] == "PING"):
            ping(line[1])
        for index, i in enumerate(line):
            #print(*line)
            if(".quit" in line[index]):
                print("Found quit command at %s" % index)
                sys.exit()
