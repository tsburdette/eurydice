import os
import json

class mailbag:
    

    def __init__(self):
        self.destpath = 'mailbag' + os.sep + 'dests.txt'
        if os.path.isfile(self.destpath):
            with open(self.destpath, 'r') as destfile:
                if (destfile.readline() != ''):
                    dests = str.split(destfile.read(), '\n')

#    def writemsg(self, msg):
        
