# required libraries
import socket

# constants
true    = 1

# Bot vars
server  = "98.252.136.71"
port    = 1993
channel = "#orpheus"
nick    = "Eurydice"
pword   = "lyric"

def ping ():
    global ircsock
    ircsock.send ("PONG : ping\n")

def sendmsg (chan, msg):
    global ircsock
    ircsock.send ("PRIVMSG " + chan + " :" + msg + "\n")

def joinchan (chan):
    global ircsock
    ircsock.send ("JOIN " + chan + "\n")

def Main():
    global ircsock

    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ircsock.connect((server, port))

    ircsock.send ("USER " + "Eurydice" + " 2 3 " + "Eurydice" + "\n")
    ircsock.send ("NICK" + nick + "\n")
    ircsock.send("QUERY AUTH PASS " + nick + ":" + pword) 
    joinchan ("#orpheus")
    while true:

        ircmsg = ircsock.recv(2048)
        ircmsg = ircmsg.strip('\n\r')
        print ircmsg
Main()
exit (0)
