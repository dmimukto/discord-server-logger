# 𝗗𝗜𝗦𝗖𝗢𝗥𝗗 𝗦𝗘𝗥𝗩𝗘𝗥 𝗟𝗢𝗚𝗚𝗘𝗥 - 𝗦𝗢𝗨𝗥𝗖𝗘
# @author dmimukto 2021
# @credits Replit's Discord Bot template, Stack Overflow, Cisc0-gif (https://github.com/Cisc0-gif/Discord-Bot-Template/blob/a53aad3ae91ed02d6f99a97328e1d9e4a9cc4a17/bot.py)
# @license MIT License (https://github.com/dmimukto/discord-server-logger/blob/main/LICENSE)
# @copyright Asenturisk Corporation 2021



# Place the chunks in the appropriate locations. I will not be held responsible if anything goes wrong.
# It's your life, your choices, your risks.
# Good luck!


# ASSUMING THAT YOU ALREADY HAVE A PROPERLY FUNCTIONAL BOT, YOU JUST NEED TO DROP IN THESE LINES OF CODE :



# This function creates/opens/writes to text files located within the vicinity of the bot's directory.
def logwrite(msg, server):
  # Have a sip of coffee as you understand that this line below basically does whatever I stated above.
  with open('Serverwise/'+str(server)+'_MESSAGES.log', 'a+') as f:
    # Voila, you have a functional read-write text file manager (not really)
    f.write(msg + '\n')
  # Remember to close your files. Why? Here's the answer : https://www.youtube.com/watch?v=6SA6S9Ca5-U (NOT MY VIDEO!)
  f.close()
  
# Labelling an event for the bot/client (use your own syntax)
@client.event
# This is the function that runs whenever your bot is ready to boogie. So merge it with your bot's on_ready() func.
async def on_ready():
  # Remove this Mukto wordmark from your code (or else something unfortunate will happen to you!)
  print("""
                                                 .-'''-.     
                                                '   _    \   
 __  __   ___                 .               /   /` '.   \  
|  |/  `.'   `.             .'|              .   |     \  '  
|   .-.  .-.   '          .'  |           .| |   '      |  ' 
|  |  |  |  |  |         <    |         .' |_\    \     / /  
|  |  |  |  |  |  _    _  |   | ____  .'     |`.   ` ..' /   
|  |  |  |  |  | | '  / | |   | \ .' '--.  .-'   '-...-'`    
|  |  |  |  |  |.' | .' | |   |/  .     |  |                 
|__|  |__|  |__|/  | /  | |    /\  \    |  |                 
               |   `'.  | |   |  \  \   |  '.'               
               '   .'|  '/'    \  \  \  |   /                
                `-'  `--''------'  '---'`'-'                  """)
  """
  The next print statements are all mostly decorative, except for the ones which don't contain useless text symbols.
  """
  print('---------------------------------------------------------------------')
  print('Server Connect Link:')
  print('https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=' + str(client.user.id))
  print('--------------------------------------------------------------------------')
  print('Logged in as:')
  print(client.user.name)
  print("or")
  print(client.user)
  print("UID:")
  print(client.user.id)
  print('---------------------------------------------')
  print("LIVE CHAT LOG - See MESSAGES.log For History")
  print("---------------------------------------------")

"""
Here we go, I'll add in proper comments to explain the functions later on.
For the time being, if you're a noob programmer, then blindly copy-paste everything. And if you're experienced, then this should be a piece o' cake for ya.
Also, if you are a Discord employee, don't proceed any further. You'll have nightmares from now on.
"""

@client.event
async def on_member_join(member):
  #channel = message.channel
  server = member.guild
  print("Member:", member, "joined!")
  #await channel.send("Member:", member, "joined 😀")
  logwrite("Member: " + str(member) + " joined!", server)
  
  if member == client.user :
    await member.send("Yo! I'm here.")
    await asyncio.sleep(30)   #The parameter is in seconds, so it'll wait for 30 seconds
    #verifiedRole = discord.utils.get(member.guild.roles, id = THE_ROLE_ID)
    #await member.add_roles(verifiedRole)

@client.event
async def on_member_remove(member):
  #channel = message.channel
  server = member.guild
  print("Member:", member, "removed!")
  #await channel.send("Member:", member, "removed 😞")
  logwrite("Member: " + str(member) + " removed!", server)

@client.event
async def on_guild_role_create(role):
  #channel = message.channel
  server = role.guild
  print("Role:", role, "was created!")
  #await channel.send("Role:", role, "was created! 📝")
  logwrite("Role: " + str(role) + " was created!", server)

@client.event
async def on_guild_role_delete(role):
  #channel = message.channel
  server = role.guild
  print("Role:", role, "was deleted!")
  #await channel.send("Role:", role, "was deleted! ❎")
  logwrite("Role: " + str(role) + " was deleted!", server)

@client.event
async def on_guild_channel_create(channel):
  #channel = message.channel
  server = channel.guild
  print("Channel:", channel, "was created!")
  #await channel.send("Channel:", channel, "was created!")
  logwrite("Channel: " + str(channel) + " was created!", server)

@client.event
async def on_guild_channel_delete(channel):
  #channel = message.channel
  server = channel.guild
  print("Channel:", channel, "was deleted!")
  #await channel.send("Channel:", channel, "was deleted!")
  logwrite("Channel: " + str(channel) + " was deleted!", server)

@client.event
async def on_guild_channel_update(before, after):
  #channel = message.channel
  server = after.guild
  print("Channel Updated:", after)
  #await channel.send("Channel Updated:", after)
  logwrite("Channel Updated: " + str(after), server)

#@client.event
#async def on_guild_join(guild):
    #guildIDs.add(guild.id)
    #print("Server/guild joined:", guild)


#@client.event
#async def on_guild_remove(guild):
    #guildIDs.remove(guild.id)
    #print("Server/guild left:", guild)


@client.event
async def on_message(message):
  if message.author == client.user:
    return #ignore what bot says in server so no message loop
  channel = message.channel
  try:
    server = channel.guild
  except:
    print("Message sent in DMs")
    server = '_privatemsg_'
  print(message.author, "said:", message.content, "-- Time:", time.ctime()) #reports to discord.log and live chat
  logwrite(str(message.author) + " said: " + str(message.content) + "-- Time: " + time.ctime(), server)
  
  
  
  # And remember to add this final statement below, if you have both client.command() commands and client.event() commands in your bot's soul.
  await client.process_commands(message)
