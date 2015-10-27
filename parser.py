import re

class parser:
    def __init__(self, text):
        # Member vars
        self.cmdWord = ''
        self.nick = ''
        self.dest = ''
        self.appendedText = ''
        # General parsing
        self.text = text
        pieces = text.split(':')
        if pieces[0] != '':
            # this means it's a server command i.e. PING
            self.cmdWord = pieces[0].strip()
            self.appendedText = pieces[1].strip()
        else:
            # we only care about commands from users for now.
            subpieces = pieces[1].split(' ')
            # therefor, there will be an address formatted as "real!~nick@address"
            if re.search('~(.*)@', subpieces[0]) is not None:
                self.nick = re.search('~(.*)@', subpieces[0]).group(1)
                # second argument is "CMD" like "PRIVMSG" or "JOIN"
                self.cmdWord = subpieces[1]
                if len(subpieces) > 2:
                    # Potentially another arg such as a channel or user
                    self.dest = subpieces[2]
                    if re.match("^(((![A-Z0-9]{5})|([#+&][^\x00\x07\r\n ,:]+))(:[^\x00\x07\r\n ,:]+)?)$", self.dest) is None:
                        # The destination arg is not a channel name. Must be a private message to the bot.
                        self.dest = self.nick
            if len(pieces) > 2:
                # anything after the second colon for PRIVMSG, PART, etc
                self.appendedText = pieces[2]
