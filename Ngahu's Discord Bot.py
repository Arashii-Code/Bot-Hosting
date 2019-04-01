import discord

TOKEN = 'XXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('go to bed'):
        msg = 'You Too {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Go to bed'):
        msg = 'You Too {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Help'):
        msg = 'If you need help Ping @Ngahu M.|2B-73'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Good Morning'):
        msg = 'Morning {0.author.mention} :D '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('good morning'):
        msg = 'Morning {0.author.mention} :D '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('goodmorning'):
        msg = 'Morning {0.author.mention} :D '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('morning'):
        msg = 'Morning {0.author.mention} :D '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('night'):
        msg = 'Good Night {0.author.mention} :) '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Night'):
        msg = 'Good Night {0.author.mention} :) '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('goodnight'):
        msg = 'Good Night {0.author.mention} :) '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('good night'):
        msg = 'Good Night {0.author.mention} :) '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Good Night'):
        msg = 'Good Night {0.author.mention} :) '.format(message)
        await client.send_message(message.channel, msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("Running")

client.run('NTYyMTkwNjAwMDkxNDY3ODA3.XKHSuw.XTMLxD4NbJ_QhCVvvXZrv9y3MS4')
