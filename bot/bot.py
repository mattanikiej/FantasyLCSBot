import discord
from discord.ext import commands
import os
import sleeper_api_calls as slp
from day_of_week import Day

# sets up client and command prefix
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='$', intents=intents)
token = os.getenv("LCS_BOT_TOKEN")

# league_id is used to identify the user's league int he Sleeper App
LEAGUE_ID = os.getenv('LEAGUE_ID')

# used to check day of week for updates
# used to make sure updates are only sent once a day
days = Day()


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


# bot uses member status updates to send in updates about standings
@client.event
async def on_member_update(before, after):
    channel = discord.utils.get(client.get_all_channels(),
                                # guild__name='TestFantasyBot',
                                name='standings-updates')

    # Monday standings update
    monday = days.check_monday()

    # Tuesday new matchups update
    tuesday = days.check_tuesday()

    # Weekend score updates
    friday = days.check_friday()
    saturday = days.check_saturday()
    sunday = days.check_sunday()

    if monday:
        monday_update = '@everyone\nMONDAY STANDINGS UPDATE\n'
        await client.get_channel(channel.id).send(monday_update + slp.get_standings(LEAGUE_ID))
    if tuesday:
        tuesday_update = '@everyone\nNEW MATCHUPS UPDATE\n'
        await client.get_channel(channel.id).send(tuesday_update + slp.get_current_matchups(LEAGUE_ID))
    # These three will be used to provide score updates once the API supports LCS scoring
    if friday:
        friday_update = '@everyone\nFRIDAY STANDINGS UPDATE\n'
        await client.get_channel(channel.id).send(friday_update + slp.get_standings(LEAGUE_ID))
    if saturday:
        saturday_update = '@everyone\nSATURDAY STANDINGS UPDATE\n'
        await client.get_channel(channel.id).send(saturday_update + slp.get_standings(LEAGUE_ID))
    if sunday:
        sunday_update = '@everyone\nSUNDAY STANDINGS UPDATE\n'
        await client.get_channel(channel.id).send(sunday_update + slp.get_standings(LEAGUE_ID))


client.run(token)
