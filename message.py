from datetime import datetime

class message:
    def __init__ (self, src, dest, body):
        self.src = src
        self.dest = dest
        self.body = body
        self.timestamp = datetime.now()

    def __str__(self):
        return "<%02d:%02d:%02d> %s: %s" % (self.timestamp.hour, self.timestamp.minute, self.timestamp.second, self.src, self.body)
