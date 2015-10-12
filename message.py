class message:
    def __init__ (self, dest, source, text):
        print "Storing message for " + dest + " from " + source
        self.dest = dest
        self.source = source
        self.text = text

    def store(self):
        with open("mailbox.txt", "w") as textfile:
            textfile.write(self.source + " " + self.dest + " " + self.text)
