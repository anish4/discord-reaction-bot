import discord
import random

client = discord.Client()

emojis = ["🔥","💥","😠", "👿", "😲", "🥑", "🍺", "🎂", "🖤", "💙", "💔", "🦋", "🤙", "📷", "✔️", "🏙️", "👏", "🤡", "🤠", "🌙", "🤞", "👑", "😢", "➗", "⬇️", "🤤", "❗", "👀", "😘", "😱", "🤭", "😷", "🙄", "😂", "♀️", "🔥", "🇧🇷", "🇮🇹", "🇪🇸", "🇺🇸", "🙏", "🍀", "☹️", "👻", "😀", "💲", "🥵", "🏠", "🤗", "💯", "♾️", "✝️", "😭", "♂️", "🤦‍♂️", "⚕️", "🦠", "🖕", "🎶", "👌", "🎉", "🥳", "🍑", "🎭", "💩", "🥺", "❓", "🌈", "🏳️‍🌈", "🙌", "🔴", "❤️", "➡️", "🤖", "🤣", "🌹", "📍", "😥", "🛡️", "🤘", "☺️", "😍", "🥰", "😈", "😊", "😎", "⚽", "✨", "⭐", "☀️", "🧸", "🤔", "👍", "💕", "☂️", "⚠️", "🤍", "😉", "🤦‍♀️", "🤷‍♀️", "🥴", "🥱"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    ff=[]
    for i in range(20):
        while True:
            emoji= emojis[random.randint(0,99)]
            if(emoji not in ff):
                await message.add_reaction(emoji)
                ff.append(emoji)
                break


        
        
client.run('your bot key ')
