from sets import Set

class skeleton:
    # Bot vars
    server      = "irc.rizon.net"
    port        = 6667
    channel     = "#orpheus"
    nick        = "Eurydice"
    nickpword   = "lyric"
    chanpword   = "transmigrationofsouls"

    chans = Set()
    mailbag = []

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
        return "USER %s %s bla :%s\r\n" % (self.nick, self.server, self.nick)
        
    def sendnick (self):
        return "NICK %s\r\n" % self.nick
        
    def sendpass (self, password):
        return "PRIVMSG NickServ IDENTIFY %s\r\n" % password
    
#    def checkmail (self, mailbag):
