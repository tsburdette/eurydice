from datetime import datetime

class message:
    def __init__ (self, source, dest, text):
        self.source = source
        self.dest = dest
        self.text = text
        self.timestamp = datetime.now()

    def tostring(self):
        return "<%02d:%02d:%02d> %s: %s" % (self.timestamp.hour, self.timestamp.minute, self.timestamp.second, self.source, self.text)
