import os
from discord.ext import commands
from discord.ext.commands import has_permissions

class AdminUtilities(commands.Cog, name='Admin Commands'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx, extension):
        if ctx.message.author.guild_permissions.kick_members:
            commands.bot.BotBase.load_extension(f'cogs.{extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        if ctx.message.author.guild_permissions.kick_members:
            commands.bot.BotBase.unload_extension(f'cogs.{extension}')
            await ctx.send("Cog: {cog} unloaded.".format(cog=extension))

    @commands.command()
    async def list(self, ctx):
        if ctx.message.author.guild_permissions.kick_members:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    await ctx.send(f'cogs.{filename[:-3]}')


def setup(client):
    client.add_cog(AdminUtilities(client))