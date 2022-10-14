import discord
from config import token
import random
import asyncio

client = discord.Client()

GUILD = ["Opal's Test Server", "The BOIS"]

siege_choice = ['Ranked', 'Unranked']

map_roll = ['Kafe Dostoyevsky', 'Chalet', 'Kanal', 'Clubhouse', 'Bank',
            'Border', 'Consulate', 'Coastline', 'Oregon', 'Outback', 'Theme Park', 'Villa']

rolling_reactions = ['Rolling...', 'Rigging...',
                    'Finishing up...', 'Stacking...']

nitro = ['Yes', 'No', 'Maybe', 'Absolutely', 'Probably not']

commands = ['?teams, - use this followed by a comma after every name to randomly generate a blue and orange team.', '?ranked or unranked - this is to randomly pick ranked or unranked',
            '?maproll - randomly selects a map from the ranked pool', '?hemmie - will hemmie be nitro\'ed?', '?nitro - Will YOU be nitro\'ed?', '?hatch - Should hemmie drop the hatch?',
            '?reroll - use this if the map is too difficult...or you just want coastline.']

reroll_map = ['Sorry! Rerolling...', 'Really? Rerolling...', 'Bruh. Rerolling...',
            'That map too difficult huh? Rerolling...', "Y'all just want coastline. Rerolling..."]


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

    if message.channel.id != 1013154771248611428:
        # handle if it's in the wrong channel here, or don't
        return

    if msg.startswith('?teams'):

        people = msg.split(',')
        people.pop(0)

        team_blue = []
        team_orange = []

        if len(people) < 10:
            while len(people) < 10:
                people.append('N/A')

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
        await message.channel.send(f'{team_blue[0]}, {team_blue[1]}, {team_blue[2]}, {team_blue[3]}, {team_blue[4]}')
        await message.channel.send('Team Orange:')
        await message.channel.send(f'{team_orange[0]}, {team_orange[1]}, {team_orange[2]}, {team_orange[3]}, {team_orange[4]}')

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

    if msg.startswith('?reroll'):
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(reroll_map))
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(map_roll))

    if msg.startswith('?hemmie'):
        await message.channel.send("Will Hemmie get nitro'ed this round?")
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(nitro))

    if msg.startswith('?nitro'):
        await message.channel.send(f"Will {message.author} get nitro'ed this round?")
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(nitro))

    if msg.lower().startswith('?hatch'):
        await message.channel.send("Should Hemmie drop the hatch?")
        time_seconds = 3
        await asyncio.sleep(time_seconds)
        await message.channel.send(random.choice(nitro))

    if msg.lower().startswith('?commands'):
        await asyncio.sleep(time_seconds)
        await message.channel.send(f'{commands[0]}\n{commands[1]}\n{commands[2]}\n{commands[3]}\n{commands[4]}\n{commands[5]}')
        

client.run(token)
