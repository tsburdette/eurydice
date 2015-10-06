# required libraries
import socket
import time
import sys
import Queue

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
    return "PONG : %s + key + \r\n" % key

def sendmsg (chan, msg):
    return "PRIVMSG %s : %s \r\n" % (chan, msg)

def joinchan (chan, password):
    return "JOIN %s %s \r\n" % (chan, password)

def senduser ():
    return "USER %s %s bla :%s\r\n" % (nick, server, nick)
    
def sendnick ():
    return "NICK %s\r\n" % nick
    
def sendpass (password):
    return "PRIVMSG NickServ IDENTIFY %s\r\n" % password

rQueue = Queue.Queue()
sQueue = Queue.Queue()

sQueue.put(senduser())
sQueue.put(sendnick())
sQueue.put(sendpass(pword))
sQueue.put("JOIN #orphtest\r\n")
sQueue.put(sendmsg("#orphtest", "Hello! I am a bot!"))

readbuffer = ""

while True:
    readbuffer = sock.recv(2048)
    temp = str.split(str.strip(readbuffer), "\r\n")
    rQueue.put(temp.pop())
    while (not rQueue.empty()):
        rx = rQueue.get()
        print rx
        rx = str.split(str.rstrip(rx))
        if (rx[0] == "PING"):
            print "Pinged!"
            sock.send(ping(rx[1]))
    if (not sQueue.empty()):
        sock.send(sQueue.get())
