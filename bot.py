import discord
import requests
import json
import datetime
from discord.ext import commands as BotBase
from discord.ext import tasks
from itertools import cycle
import os

intents = discord.Intents().all()
bot = BotBase.Bot(command_prefix='&db ', intents=intents)

#bot_token_dev = 'ODI0MTA0MzQyMTA0OTY1MTQw.YFqg-g.hWil2bYsL7Mat82U6mBi1Ma3zoU'
bot_token = 'ODIyNjgxMjM2NTM5NDQxMTc0.YFVzmw.jk2vKQfXdbzUW6jrHIszCyGau5g'
act = cycle([discord.Game, discord.Game, discord.Game])

@bot.event
async def on_ready():
    bot.statuses = cycle(['Mstir Hub | &db help'])
    change_status.start()
    find_online_members.start()

@tasks.loop(seconds=17)
async def change_status():
    await bot.wait_until_ready()
    await bot.change_presence(activity=next(act)(name=next(bot.statuses)))

@tasks.loop(seconds=30)
async def find_online_members():
        await bot.wait_until_ready()
        url = requests.get('https://rbx.jmk.gg/getOnline')
        data = json.loads(url.text)
        channel = bot.get_channel(835756115467173899)
        roles = {'4199740': 'video star', 'dev': 'developer', '1200769': 'Administrator'}
        found = True

        embed = discord.Embed(title="Dohm Industries Metaverse Box Finder",
                              description="This an up-to-date list of all Video Stars, Developers and Administrations currently [online](https://www.google.com) in the Metaverse Champion Hub. This list updates every 2 minutes, Click on the profile link then click **Join Game**.",
                              color=0xbf9626)


        for groupId in data:
            status = data[groupId]
            for keys in status:
                    if keys and keys['placeId'] == 6674394294:
                        for i in roles:
                            if i in groupId:
                                found
                                role = roles[i]
                                print(role)
                                embed.add_field(name="{name} - {role}".format(name=keys['user']['name'], role=role), value="[profile](https://www.roblox.com/users/{url}/profile)".format(url=keys['user']['userId']), inline=False)
                                embed.set_thumbnail(url="https://i.ibb.co/G5Bqrkg/box.png")
                                embed.set_footer(text="Property of Dohm Industries ©️")
                                embed.timestamp = datetime.datetime.utcnow()
                                msg = await channel.fetch_message(835756657833148416)
                                await msg.edit(embed=embed)
                            elif roles[i] is None:
                                embed.add_field(name="No Users Found", value="but here are some pictures of [kittens](http://www.randomkittengenerator.com) to enjoy while you wait!", inline=True)
                                embed.set_thumbnail(url="https://i.ibb.co/G5Bqrkg/box.png")
                                embed.set_footer(text="Property of Dohm Industries ©️")
                                embed.timestamp = datetime.datetime.utcnow()
                                msg = await channel.fetch_message(835756657833148416)
                                return await msg.edit(embed=embed)












@find_online_members.before_loop
async def before():
    print('Starting loop')



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Hey man, you dropped an argument, you better pick it up! [Missing Argument Error]")

@bot.listen('on_message')
async def do_stuff(message):
    mention = f'<@!{bot.user.id}>'
    if mention in message.content:
        embedVar = discord.Embed(title="Bot Information",
                                 description="Hey, hows it going my name is DohmBot :)\nI started out as a way to get information from forums.robloxscripts.com.\nMy functionality is ever growing into a entertainment based bot.",
                                 color=0xbf9626)
        embedVar.add_field(
            name='Bot Prefix',
            value="&db",inline=False)

        embedVar.add_field(
            name='Help Command',
            value="&db help",inline=False)

        embedVar.add_field(
            name='Bot Creator',
            value="[DohmBoyOG](https://forum.robloxscripts.com/User-DohmBoy64)",inline=False)

        embedVar.add_field(
            name='Website',
            value="[Available Here](https://www.dohmscripts.com)", inline=False)

        embedVar.set_footer(text='Property of Dohm Industries ©')
        await message.channel.send(embed=embedVar)
        #await message.channel.send("{user}".format(user=message.author.mention))

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(f"Pong!  `{int(latency)}ms`")

@bot.command()
async def ping_exact(ctx):
    latency = bot.latency
    await ctx.send(f"Pong!  `{(latency)}ms`")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(bot_token)



