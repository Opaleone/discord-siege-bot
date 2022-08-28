import discord
from config import token
import random
import asyncio


client = discord.Client()

GUILD = ["Opal's Test Server", "The BOIS"]

siege_choice = ['Ranked', 'Unranked']

map_roll = ['Kafe Dostoyevsky', 'Chalet', 'Kanal', 'Clubhouse', 'Bank',
            'Border', 'Consulate', 'Coastline', 'Oregon', 'Outback', 'Theme Park', 'Villa']

rolling_reactions = ['Rolling...', 'Rigging...', 'Finishing up...', 'Stacking...']

hemmie = ['Yes', 'No', 'Maybe', 'Absolutely', 'Probably not']

commands = ['?teams, - use this followed by a comma after every name to randomly generate a blue and orange team.(must be 10 names)', '?ranked or unranked - this is to randomly pick ranked or unranked',
            '?maproll - randomly selects a map from the ranked pool', "?nitro - will hemmie be nitro'ed?", '?hatch - Should hemmie drop the hatch?']


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to the following server: \n'
          f'{guild}(id: {guild.id})')

    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name='for Siege requests...'))


@client.event
async def on_message(message):
    msg = message.content
    people = []
    time_seconds = 1

    if message.author == client.user:
        return

    if msg.startswith('?teams'):

        people = msg.split(',')
        people.pop(0)

        team_blue = []
        team_orange = []

        for i in range(5):
            one = random.choice(people)
            team_blue.append(one)
            people.remove(one)

        for i in range(5):
            two = random.choice(people)
            team_orange.append(two)
            people.remove(two)

        await message.channel.send(random.choice(rolling_reactions))
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send('Team Blue:')
        await message.channel.send(team_blue)
        await message.channel.send('Team Orange:')
        await message.channel.send(team_orange)

    if msg.startswith('?ranked or unranked'):
        await asyncio.sleep(time_seconds)
        await message.channel.send('Rolling...')
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(siege_choice))

    if msg.startswith('?map roll'):
        await asyncio.sleep(time_seconds)
        await message.channel.send('Rolling...')
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(map_roll))

    if msg.startswith('?nitro'):
        await message.channel.send("Will Hemmie get nitro'ed this round?")
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(hemmie))

    if msg.lower().startswith('?hatch'):
        await message.channel.send("Should Hemmie drop the hatch?")
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(hemmie))

    if msg.lower().startswith('?commands'):
        await message.channel.send(commands[0])
        await message.channel.send(commands[1])
        await message.channel.send(commands[2])
        await message.channel.send(commands[3])
        await message.channel.send(commands[4])

client.run(token)