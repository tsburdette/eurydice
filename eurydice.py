# required libraries
import socket
import time
import sys
import Queue

from skeleton import skeleton
from dialogue import dialogue

bot = skeleton()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((bot.server, bot.port))

rQueue = Queue.Queue()
sQueue = Queue.Queue()

sQueue.put(bot.senduser())
sQueue.put(bot.sendnick())
#sQueue.put(bot.joinchan("#orpheus", "transmigrationofsouls"))

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
#        if ("JOIN" in rx[1]):
        if (len(rx) == 3 and "PRIVMSG" in rx[1]):
            rxDiag = str.split(str.rstrip(rx[1]))
            cmd = dialogue(rxDiag[0], rxDiag[2], rx[2], bot)
            tx = cmd.respond()
            if (tx != ""):
                sQueue.put(tx)
    if (not sQueue.empty()):
        tx = sQueue.get()
        print ">> " + tx
        sock.send(tx)
