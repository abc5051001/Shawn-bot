
import discord


client = discord.Client()

f = open("token.txt")
TOKEN = f.readline()
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!Hi'):
        await message.channel.send('Hey')


client.run(TOKEN)
