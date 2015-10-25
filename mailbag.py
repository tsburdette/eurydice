import os
import json
import re

class mailbag:
    
    def __init__(self):
        self.destpath = 'mailbag' + os.path.sep + 'destinations.txt'
        self.bodypath = 'mailbag' + os.path.sep + 'bodies.txt'
        self.relpath = 'mailbag' + os.path.sep + 'relations.txt'
        self.dests = []
        self.bodies = []
        self.relations = []
        if os.path.isfile(self.destpath):
            with open(self.destpath, 'r') as destfile:
                self.dests = destfile.read().splitlines()
        if os.path.isfile(self.bodypath):
            with open(self.bodypath, 'r') as bodyfile:
                self.bodies = bodyfile.read().splitlines()
        if os.path.isfile(self.relpath):
            with open(self.relpath, 'r') as relfile:
                self.relations = relfile.read().splitlines()

    def storemsg(self, msg):
        msgdest = msg.dest
        msgbody = msg.__str__()
        if msgdest not in self.dests:
            self.dests.append(msgdest)
        if msgbody not in self.bodies:
            self.bodies.append(msgbody)
        destindex = self.dests.index(msgdest)
        bodyindex = self.bodies.index(msgbody)
        relstring = '%d %d' % (destindex, bodyindex)
        if relstring not in self.relations:
            self.relations.append(relstring)
            
    def retrievemsgs(self, msgdest):
        destindex = self.dests.index(msgdest)
        messages = []
        for index, relstring in enumerate(self.relations):
            if relstring.find(str(destindex)) == 0:
                bodyindex = re.search(' (.*)', relstring).group(1)
                messages.append(self.bodies[int(bodyindex)])
        return messages
        
    def writeall(self):
        with open(self.destpath, 'w') as destfile:
            for destline in self.dests:
                destfile.write(destline + '\n')
        with open(self.bodypath, 'w') as bodyfile:
            for bodyline in self.bodies:
                bodyfile.write(bodyline + '\n')
        with open(self.relpath, 'w') as relfile:
            for relstring in self.relations:
                relfile.write(relstring + '\n')