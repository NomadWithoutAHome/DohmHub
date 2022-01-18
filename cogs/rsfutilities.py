import discord
import requests
import json
from helpers.userData import userdata_from_dict
from helpers.threadData import latestdata_from_dict
from discord.ext import commands
import json
import requests


class Rsfutilities(commands.Cog, name='Forum commands'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    @commands.command(name='find',help="Use &db find [name]  EX: dohmboy64, to look them up and you can click on the name to view the profile on the forums.", brief="brief overview of a user")
    async def forumUserLookUp(self, ctx, *, args):

        url = requests.get('http://roblox-forums.herokuapp.com/api/robloxscriptsforums/userlookup?name={usr}'.format(usr=args))

        if not '1911' in url.text:
            data = userdata_from_dict(url.json())

            print(data.joindate)

            embedVar = discord.Embed(title="This User At A Glance",
                                     description="Gives you a quick glance of the bankdb forums.robloxscripts.com profile.",
                                     color=0xbf9626)

            embedVar.add_field(
                name='Rep:',
                value="[{userrep}](https://forum.robloxscripts.com/{replink})".format(userrep=data.rep, replink=data.replink),
                inline=True)

            embedVar.add_field(
                name='Join Date:',
                value="{date}".format(date=data.joindate), inline=True)

            embedVar.add_field(
                name='Status:',
                value="[{stats}](https://forum.robloxscripts.com/online.php)".format(stats=data.status), inline=True)

            embedVar.add_field(
                name='Threads:',
                value="[{threads}](https://forum.robloxscripts.com/{threadlink})".format(threads=data.threads,
                                                                                         threadlink=data.threadlink),
                inline=True)

            embedVar.add_field(
                name='Posts:',
                value="[{pst}](https://forum.robloxscripts.com/{postlink})".format(pst=data.posts, postlink=data.postlink),
                inline=True)

            embedVar.add_field(
                name='Recent Activity:',
                value="{actt}".format(actt=data.active), inline=True)

            embedVar.add_field(
                name='How long has this user spend online:',
                value="{timeonline}".format(timeonline=data.timeonline.replace('i have spent', '')), inline=True)

            embedVar.set_author(
                name='{name}'.format(name=data.username),
                url="{u}".format(u=data.proflink),
                icon_url='{pfp}'.format(pfp=data.pfp))
            await ctx.send(embed=embedVar)
        else:
            await ctx.send('you may have spelled the username wrong or there is no user with that name.')\

    @commands.command(name='latest',help="Gets the Latest Threads From forums.robloxscripts.com, updates every 30 minutes.", brief="Gets the latest threads.")
    async def getLatestThreads(self, ctx):
        url = requests.get(
        'http://roblox-forums.herokuapp.com/api/robloxscriptsforums/latest-threads')
        tdata = latestdata_from_dict(json.loads(url.text))
        embedVar = discord.Embed(title="The Latest Roblox Script Forums Threads",
                             description="Gets the latest threads on forums.robloxscripts.com [Live View]",
                             color=0xbf9626)

        for i in tdata.latest:
            embedVar.add_field(
                name='{post} by {user} about ({time})'.format(post=i.title, user=i.author, time=i.time),
                value="[Thread Link]({link})".format(link=i.url), inline=False)
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Rsfutilities(client))