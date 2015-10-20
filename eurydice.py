# required libraries
import socket
import time
import sys
import Queue
from dialogue import dialogue
from sets import Set

# Bot vars
server      = "irc.rizon.net"
port        = 6667
channel     = "#orpheus"
nick        = "Eurydice"
nickpword   = "lyric"
chanpword   = "transmigrationofsouls"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))
class Eurydice:
    chans = Set()

    def ping (self, key):
        return "PONG %s \r\n" % key

    def sendmsg (self, chan, msg):
        return "PRIVMSG %s :%s \r\n" % (chan, msg)

    def joinchan (self, chan, password=""):
        self.chans.add(chan)
        return "JOIN %s %s \r\n" % (chan, password)

    def partchan (self, chan):
        self.chans.discard(chan)
        return "PART %s \r\n" % (chan)

    def senduser (self):
        return "USER %s %s bla :%s\r\n" % (nick, server, nick)
        
    def sendnick (self):
        return "NICK %s\r\n" % nick
        
    def sendpass (self, password):
        return "PRIVMSG NickServ IDENTIFY %s\r\n" % password

rQueue = Queue.Queue()
sQueue = Queue.Queue()

bot = Eurydice()

sQueue.put(bot.senduser())
sQueue.put(bot.sendnick())
sQueue.put(bot.sendpass(nickpword))
sQueue.put(bot.joinchan(channel,chanpword))
#sQueue.put("JOIN #orpheus transmigrationofsouls\r\n")
#sQueue.put(bot.sendmsg("#orphtest", "Hello! I am Eurydice, a bot! Say my name!"))

readbuffer = ""

while True:
    readbuffer = sock.recv(2048)
    temp = str.split(str.strip(readbuffer), "\r\n")
    rQueue.put(temp.pop())
    while (not rQueue.empty()):
        rx = rQueue.get()
        print rx
        rx = str.split(str.rstrip(rx), ":", 2)
        if ("PING" in rx[0]):
            print bot.ping(rx[1])
            sock.send(bot.ping(rx[1]))
        if (len(rx) == 3 and "PRIVMSG" in rx[1]):
            rxDiag = str.split(str.rstrip(rx[1]))
            cmd = dialogue(rxDiag[0], rxDiag[2], rx[2], bot)
            tx = cmd.respond()
            if (tx != ""):
                sQueue.put(tx)
    if (not sQueue.empty()):
        tx = sQueue.get()
        print ">> "+ tx
        sock.send(tx)
