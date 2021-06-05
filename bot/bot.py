import discord
from discord.ext import commands
import os
import sleeper_api_calls as slp

# sets up client and command prefix
client = commands.Bot(command_prefix='$')
token = os.getenv("LCS_BOT_TOKEN")

# league_id is used to identify the user's league int he Sleeper App
LEAGUE_ID = os.getenv('LEAGUE_ID')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Demoting to Wood IV"))


# command $standings displays the current standings of the league
@client.command()
async def standings(ctx):
    await ctx.send(slp.get_standings(LEAGUE_ID))


# command $matchups will display all of the current scores of the week
@client.command()
async def matchups(ctx):
    await ctx.send(slp.get_current_matchups(LEAGUE_ID))

client.run(token)
