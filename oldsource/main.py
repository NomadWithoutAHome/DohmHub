from itertools import cycle
from discord.ext import commands
import discord
import json
import requests
import getForumInfo
from discord.ext import tasks
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='&db ')
TOKEN = 'ODIyNjgxMjM2NTM5NDQxMTc0.YFVzmw.jk2vKQfXdbzUW6jrHIszCyGau5g'

act = cycle([discord.Game, discord.Game, discord.Game])


@bot.event
async def on_ready():
    bot.statuses = cycle(['Mstir Hub | &db help'])
    change_status.start()
    update_threads.start()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Hey man, you dropped an argument, you better pick it up! [Missing Argument Error]")


@tasks.loop(seconds=17)
async def change_status():
    await bot.wait_until_ready()
    await bot.change_presence(activity=next(act)(name=next(bot.statuses)))


@tasks.loop(minutes=30.0)
async def update_threads():
    requests.get(
        'https: // simplescraper.io / api / Y1tButjWBX2ccsoWjrux?apikey = Vmp3N92A2U7BdZSyGiq9XY16qYNrET2N & run_now = true & limit = 100')


@update_threads.after_loop
async def after_threads_update():
    print('Done Updating Threads')


@bot.command(help="What? you expected more help for this command? pssh..loser", brief="Prints pong back to the channel.")
async def ping(ctx):
    await ctx.send('pong!')


@bot.command(name='latest',help="Gets the Latest Threads From forums.robloxscripts.com, updates every 30 minutes.", brief="Gets the latest threads from the forums.")
async def getLatestThreads(ctx):
    url = requests.get(
        'https://simplescraper.io/api/Y1tButjWBX2ccsoWjrux?apikey=Vmp3N92A2U7BdZSyGiq9XY16qYNrET2N&limit=100')
    results = getForumInfo.latest_threads_from_dict(json.loads(url.text))
    embedVar = discord.Embed(title="The Latest Roblox Script Forums Threads",
                             description="Gets the latest threads on forums.robloxscripts.com [Updates Every 30 Minutes]",
                             color=0x00ff00)
    for i in results.data:
        embedVar.add_field(
            name='{post} by {user} about ({time})'.format(post=i.post_title, user=i.post_user, time=i.post_time),
            value="[Thread Link]({link})".format(link=i.post_title_link), inline=False)
    await ctx.send(embed=embedVar)


@bot.command(name='invites',help="Use Hey DohmBot give_me_discord_invite [name], Options: mstir and grubhub", brief="Gives you invites to Friends of DohmBoyOG Servers")
async def getDiscordInvites(ctx, args):
    loweredargs = args.lower()
    if loweredargs == 'mstir':
        await ctx.send('https://discord.gg/C2VZBYdqEd')
    elif loweredargs == 'grubhub':
        await ctx.send('https://discord.gg/fyUVHeeNEh')
    else:
        await ctx.send('They are not  D O P E enough or you spelled it wrong!')


@bot.command(name='find',help="Use &db find [name]  EX: dohmboy64, to look them up and you can click on the name to view the profile on the forums.", brief="brief overview of a user on the forums")
async def forumUserLookUp(ctx, args):
    url = requests.get('https://forum.robloxscripts.com/User-{usr}'.format(usr=args))
    soup = BeautifulSoup(url.content, 'html.parser')
    print(url.url)
    if not 'The member you specified is either invalid' in soup.text:
        name = soup.select_one(
        '#content > div.wrapperforum > div.container.bootstrap.snippet > div > div > div.profile-cover-statss3.mobile-hide > span.largetext > strong').text.strip()
        pfp = soup.select_one('div.author-info-img img.profileavatarst')['src']
        try:
            rep = soup.select_one('.reputation_positive').text.strip()
        except AttributeError:
            try:
                rep = soup.select_one('.reputation_negative').text.strip()
            except AttributeError:
                rep = 'no/neutral'
        threads = soup.select_one(':nth-child(1) > .stats-num-cover > a').text.strip()
        posts = soup.select_one(':nth-child(2) > .stats-num-cover > a').text.strip()
        replink = soup.select_one('#content > div.wrapperforum > div:nth-child(9) > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(1) > div.profile-top > span > strong > center > strong > a')['href']
        timeonline = soup.select_one('#content > div.wrapperforum > div:nth-child(9) > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(8)').text.strip().lower()
        threadlink = soup.select_one('#content > div.wrapperforum > div.container.bootstrap.snippet > div > div > div.profile-cover-statss1 > div > div:nth-child(1) > div > a')['href']
        postlink = soup.select_one('#content > div.wrapperforum > div.container.bootstrap.snippet > div > div > div.profile-cover-statss1 > div > div:nth-child(2) > div > a')['href']

        try:
            active = soup.select_one('#content > div.wrapperforum > div.container.bootstrap.snippet > div > div > div.profile-cover-statss3.mobile-hide > span.onmobile').text.strip('()')
        except AttributeError:
            active = "no recent activity"

        try:
            status = soup.select_one(
            '#content > div.wrapperforum > div.container.bootstrap.snippet > div > div > div.profile-cover-statss3.mobile-hide > a > span').text.strip()
        except AttributeError:
            try:
                status = soup.select_one('#content > div.wrapperforum > div.container.bootstrap.snippet > div > div > div.profile-cover-statss3.mobile-hide > span.offline').text.strip()
            except AttributeError:
                print('need to fix api')

        embedVar = discord.Embed(title="This User At A Glance",
                             description="Gives you a quick glance of the bankdb forums.robloxscripts.com profile.",
                             color=0x00ff00)

        embedVar.add_field(
        name='Rep:',
        value="[{userrep}](https://forum.robloxscripts.com/{replink})".format(userrep=rep,replink=replink), inline=True)

        embedVar.add_field(
        name='Thanks:',
        value="WIP", inline=True)

        embedVar.add_field(
        name='Status:',
        value="[{stats}](https://forum.robloxscripts.com/online.php)".format(stats=status), inline=True)

        embedVar.add_field(
        name='Threads:',
        value="[{threads}](https://forum.robloxscripts.com/{threadlink})".format(threads=threads,threadlink=threadlink), inline=True)

        embedVar.add_field(
        name='Posts:',
        value="[{pst}](https://forum.robloxscripts.com/{postlink})".format(pst=posts,postlink=postlink), inline=True)

        embedVar.add_field(
            name='Recent Activity:',
            value="{actt}".format(actt=active),inline=True)

        embedVar.add_field(
        name='How long has this user spend online:',
        value="{timeonline}".format(timeonline=timeonline.replace('i have spent', '')), inline=True)

        embedVar.set_author(
        name='{name}'.format(name=name),
        url="https://forum.robloxscripts.com/User-{ul}".format(ul=args),
        icon_url= '{pfp}'.format(pfp=pfp))

        await ctx.send(embed=embedVar)
    else:
        await ctx.send('Hey man, you either spelled the name wrong or the user is invalid')



@bot.listen('on_message')
async def do_stuff(message):
    mention = f'<@!{bot.user.id}>'
    if mention in message.content:
        await message.channel.send("Yo, Dawg! whadda ya want. {user}".format(user=message.author.mention))


bot.run(TOKEN)
