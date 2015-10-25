import re
import pdb
from message import message
from mailbag import mailbag

class dialogue:
    cmds = [ "tell", "status", "help", "join", "part" ]
    sack = mailbag()
    
    def __init__ (self, user, channel, text, bot):
        print text
        self.user = user
        self.channel = channel
        self.text = text
        self.bot = bot
        
    def respond (self):
        if (self.text.find("!help") == 0):
            info = str.split(self.text, ' ', 1)
            if (len(info) == 1):
                msg1 = "My commands are " + str(self.cmds)[1:-1]
                msg2 = "For help with a specific command, type \'!help <command>\'."
                return self.bot.sendmsg(self.channel, msg1) + self.bot.sendmsg(self.channel, msg2)
            else:
                return self.bot.sendmsg(self.channel, self.cmdhelp(info[1]))
        if (self.text.find("!tell") == 0):
            info = str.split(self.text, ' ', 2)
            mail = message(self.user, info[1], info[2])
            self.sack.storemsg(mail)
            msg = "Storing message for " + info[1]
            self.sack.writeall()
            return self.bot.sendmsg(self.channel, msg)
        if (self.text.find("!getmessages") == 0):
            requester = re.search('~(.*)@', self.user).group(1)
            msgs = self.sack.retrievemsgs(requester)
            output = ""
            for line in msgs:
                output += self.bot.sendmsg(requester, line)
            return output
        if (self.text.find("!status") == 0):
            info = str.split(self.text, ' ', 1)
            msg = "I should really get around to watching " + info[1]
            return self.bot.sendmsg(self.channel, msg)
        if (self.text.find("!join") == 0):
            info = str.split(self.text, ' ', 2)
            pword = ""
            if len(info) == 3:
                pword = info[2]
            if (re.match("^(((![A-Z0-9]{5})|([#+&][^\x00\x07\r\n ,:]+))(:[^\x00\x07\r\n ,:]+)?)$", info[1])):
                msg = "Joining " + info[1]
                return self.bot.sendmsg(self.channel, msg) + self.bot.joinchan(info[1], pword)
            else:
                msg = "That's not a valid channel to join. Sorry."
                return self.bot.sendmsg(self.channel, msg)
        if (self.text.find("!part") == 0):
            info = str.split(self.text, ' ', 1)
            if ((re.match("^(((![A-Z0-9]{5})|([#+&][^\x00\x07\r\n ,:]+))(:[^\x00\x07\r\n ,:]+)?)$", info[1]) is not None) & (info[1] in self.bot.chans)):
                msg = "Parting " + info[1]
                return self.bot.sendmsg(self.channel, msg) + self.bot.partchan(info[1])
            else:
                msg = "That channel may not be valid or I'm not in that channel. Try again, please."
                return self.bot.sendmsg(self.channel, msg)
        return ""
        
    def cmdhelp (self, text):
        print "cmd: " + text
        if (text == "help"):
            return "You're already using help."
        elif (text == "tell"):
            return "The format for !tell is \'!tell <person> <msg>\'. Undelivered messages are not currently encrypted, but that will be implemented. I do not archive your messages after they have been delivered."
        elif (text == "status"):
            return "!status doesn't do what it's supposed to yet, but you can use \'!status <show name>\' for now."
        elif (text == "join"):
            return "The format for !join is \'!join <channel> <password>\'. The password field is optional, and be careful since obviously the string will be visible to my owner, Fomalhaut. I don't encrypt those yet."
        elif (text == "part"):
            return "The format for !part is \'!part <channel>\'. I will not recall a password on a rejoin. You'll have to provide it again."
        else:
            return "I don't recognize that command. Make sure you spelled it correctly. For a list of commands, type just \'!help\'."
