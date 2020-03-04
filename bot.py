import discord
from time import sleep

class bot(discord.Client):
    async def on_ready(self):
        discord.opus.load_opus("/home/linuxbrew/.linuxbrew/Cellar/opus/1.3.1/lib/libopus.so")
        print('Logged on as: ' + self.user.display_name)
        print('Bot latency: ' + str(self.latency))
        print('Opus is loaded: ' + str(discord.opus.is_loaded()))
        self.userBlackList = []
        self.sym = '!'
    
    async def on_message(self, message):
        hasMention = False
        author = message.author
        msgc = message.content
        guild = message.guild
        # if is a private msg, use another handler
        if not message.guild:
            dmHandler(self, message)
            return

        # checks for the message author
        if message.author.bot == True or message.author.system == True:
            return # if is a bot or is a system message ignore it
        elif message.author in self.userBlackList:
            return # ignore users in the blacklist
        # check the message
        if not ( msgc.startswith(self.sym) or msgc.find(self.sym) == 0 ):
            return # ignore normal message
        
        # convert the message to lower case and
        # split the message in command and variable
        sc = msgc.find(" ")
        try:
            command, variable = msgc.split(maxsplit=1)
            command = command.lower().lstrip()
        except:
            command = msgc.lower().lstrip()
            variable = None
        # remove the symbol from the command
        command = command.replace(self.sym, "", 1)
        # check if the message has mentions
        if message.mentions:
            hasMention = True
        # now its all ready to be used!
        # log the message
        print("command: {0}, variable: {1}, sender: {2}, guild: {3}, has mention: {4}".format(command, variable, author, guild, hasMention))
        # process the commands
        if command in ["about","info"]:
            await embed(message, "About me", "I'm a bot built for testing and learning more python\nProgramming Language: Python\nLibraries: discord.py, requests\nAuthor: ENDERZOMBI102\nLibopus: {opus}".format(opus=discord.opus.is_loaded()))
        elif command in ["connect","join","play","p","stop","reset",]:
            await self.musicPlayer(message, command, variable)
        elif command in "i":
            pass
    
    async def musicPlayer(self, msgObj, command, variable):
        if not discord.opus.is_loaded():
            embed(msgObj, "ERROR", "LibOpus isn't loaded, can't use voice", "red")
        if command in ["connect", "c", "join", "j"]:
            if False:
                pass

async def dmHandler(self, message):
    pass

async def embed(msgObj=None, title=None, message=None, colorA="white"):
    embedMsg = discord.Embed(title = title, description = message, color = giveMeColor(colorA))
    await msgObj.channel.send(embed = embedMsg)

def giveMeColor(color):
    r"""
        this function return the hex value of the requested color
    """
    if color == "red":
        return 0xFF0000
    elif color == "green":
        return 0x008000
    elif color == "yellow":
        return 0xffff00
    elif color == "white":
        return 0xffffff
    elif color == "black":
        return 0x000000
    elif color == "lime":
        return 0x00ff00
    elif color == "blue":
        return 0x0000ff
    elif color == "cyan":
        return 0x00ffff
    elif color == "magenta":
        return 0xff00ff
    elif color == "gray":
        return 0x808080







client = bot()
client.run("NjAzNjk1NTYxOTc1MjY3MzM4.XaY90Q.Mv2DK4VQPWdAIZeGwCHp_zTPHAU")