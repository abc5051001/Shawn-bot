
import discord
import random
from discord.ext import commands


f = open("token.txt")
TOKEN = f.readline()

client = commands.Bot(command_prefix = '!')

## events
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

## commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Yuor ping is :{round(client.latency) * 1000}ms')

@client.command(aliases=['8ball','question']) # all words in aliases can be used for this command
async def _8ball(ctx, *, question):
    responses =["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\n Answer:{random.choice(responses)}')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)


client.run(TOKEN)
