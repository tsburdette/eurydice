import re
from datetime import datetime

class message:
    def __init__ (self, parser):
        self.src = parser.nick
        self.dest = parser.dest
        self.body = parser.appendedText
        # TODO: CTCP command to get sender's current time.
        self.timestamp = datetime.now()

    def __str__(self):
        return "<%02d:%02d:%02d> %s: %s" % (self.timestamp.hour, self.timestamp.minute, self.timestamp.second, self.src, self.body)
