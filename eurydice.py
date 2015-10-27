# required libraries
import socket
import time
import sys
import Queue
import pdb
from skeleton import skeleton
from dialogue import dialogue
from parser import parser

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
        rxParsed = parser(rx)
        if (rxParsed.cmdWord == "PING"):
            # prioritize PING responses
            print bot.ping(rxParsed.appendedText)
            sock.send(bot.ping(rxParsed.appendedText))
#        if (rxParsed.cmdWord == "JOIN"):
            # TODO: if bot.checkMail():
            #    send user alert to check mail
        if (rxParsed.cmdWord == "PRIVMSG"):
            cmd = dialogue(rxParsed, bot)
            tx = cmd.respond()
            if (tx != ""):
                sQueue.put(tx)
    if (not sQueue.empty()):
        # send any queued up commands
        tx = sQueue.get()
        print ">> " + tx
        sock.send(tx)
    
