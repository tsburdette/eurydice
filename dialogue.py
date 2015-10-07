class dialogue:
    def __init__ (self, user, channel, text, bot):
        print text
        self.user = user
        self.channel = channel
        self.text = text
        self.bot = bot
        
    def respond (self):
        if ("Eurydice" in self.text):
            return self.bot.sendmsg(self.channel, "I hear you!")
        return ""