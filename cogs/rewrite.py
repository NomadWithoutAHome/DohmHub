import discord
import json
import os
from datetime import datetime
from datetime import date
from discord.ext import commands
from secrets import token_hex

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, f'../data/bankdb.json')


today = date.today()
now = datetime.now()


class Rewrite(commands.Cog, name='Economy Commands'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pay(self, ctx, account: discord.User, money):
        transid = token_hex()
        time = now.strftime("%H:%M:%S")
        date = today.strftime("%m/%d/%Y")

        users = await self.get_bank_data()
        print('here')
        if not str(account.id) in users:
            bankteller = discord.Embed(
                description='Hey {usr}, i wanted to inform you there was a banking error, i cannot transfer fund because {sendto} do not have an account on file with us.'.format(
                    usr=ctx.author.name, sendto=account),
                color=0xbf9626)
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await ctx.author.send(embed=bankteller)

        elif not str(ctx.author.id) in users:
            bankteller = discord.Embed(
                description='Hey {usr}, it seems you are trying to transfer funds but we do not have an account on file for you, not a problem to create an account use &db create_account.'.format(
                    usr=ctx.author.name, sendto=account),
                color=0xbf9626)
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await ctx.author.send(embed=bankteller)
        elif int(money) < 0:
            bankteller = discord.Embed(
                description='Hey {usr}, when transferring funds to another account you must use positive numbers only.'.format(
                    usr=ctx.author.name),
                color=0xbf9626)
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await ctx.author.send(embed=bankteller)
        elif int(money) > users[str(ctx.author.id)]['wallet']:
            bankteller = discord.Embed(
                description='Hey {usr}, i wanted to let you know that you wanted to transfer {trans} but you only have {current} in your account, so i can now process your transfer request right now'.format(
                    trans=money, current=users[str(ctx.author.id)]['wallet'], usr=ctx.author),
                color=0xbf9626)
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await ctx.author.send(embed=bankteller)
        else:
            users[str(ctx.author.id)]['wallet'] -= int(money)
            users[str(account.id)]['wallet'] += int(money)
            users[str(ctx.author.id)]['transactions'].insert(0, {transid: {"type": 'payment', "amount": money, "date": date, "time": time, "payee": account.id}})


            with open(my_file, 'w') as f:
                json.dump(users, f)

            bankteller = discord.Embed(
                description='Hey {usr}, i just wanted to let you know that someone initiated a transfer of funds into your account and that i finished proccessing it, the details can be found below, have a blessed day!'.format(
                    usr=account),
                color=0xbf9626)
            bankteller.add_field(name='Payee:', value='{sender}'.format(sender=ctx.author))
            bankteller.add_field(name='Amount:', value='{money} (Dc)'.format(money=money))
            bankteller.add_field(name='Current Balance:', value='{money} (Dc)'.format(
                money=users[str(str(account.id))]['wallet']))
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await account.send(embed=bankteller)

            bankteller = discord.Embed(
                description='Hey {usr}, i just finished processing your request, the details are down below, have a blessed day!'.format(
                    usr=ctx.author),
                color=0xbf9626)
            bankteller.add_field(name='Paid:', value='{sender}'.format(sender=account))
            bankteller.add_field(name='Amount:', value='{money} (Dc)'.format(money=money))
            bankteller.add_field(name='Current Balance:', value='{money} (Dc)'.format(
                money=users[str(str(ctx.author.id))]['wallet']))
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await ctx.author.send(embed=bankteller)

    @commands.command()
    async def create(self, ctx):
        print('create')
        await self.create_account(ctx.author)

    async def get_bank_data(self):
        with open(my_file, 'r') as f:
            users = json.load(f)
        return users

    async def create_account(self, user):
        transid = token_hex()
        time = now.strftime("%H:%M:%S")
        date = today.strftime("%m/%d/%Y")

        users = await self.get_bank_data()
        print(users)
        if not await self.check_if_exists(str(user.id)):
            users[str(user.id)] = {"transactions": []}
            users[str(user.id)]['wallet'] = 1000
            users[str(user.id)]['hash'] = token_hex(5)
            users[str(user.id)]['joindate'] = today.strftime("%m/%d/%Y")
            users[str(user.id)]['transactions'].append({transid: {"type": 'payment', "amount": 10000, "date": date, "time": time, "payee": 'Dohm Industries'}})


            with open(my_file, 'w') as f:
                json.dump(users, f)

            bankteller = discord.Embed(
                description='Thank you for choosing Dohm Industries Savings and Loans.\nmy name is Jenny, from here on out I will be your personal bank teller, and because your a new account i have deposited 1000dc into your account!\n\ni am sending you, your account holder card, remember to always keep it safe as DISL will NEVER ask for your account ID over text or email!"',
                color=0xbf9626)
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await user.send(embed=bankteller)

            bankteller = discord.Embed(description='Account Holder Card', color=0xbf9626)
            bankteller.add_field(name='Name:', value=user.name, inline=True)
            bankteller.add_field(name='Account ID:', value='{acid}'.format(acid=token_hex(5)))
            bankteller.set_thumbnail(url=user.avatar_url)
            bankteller.set_footer(text='Dohm Industries Saving and Loans™️')
            await user.send(embed=bankteller)
        else:
            bankteller = discord.Embed(
                description='Hey {usr}, i noticed you already have an account on file with us, which is GREAT, but unfortunately that means i am not able to created another account for you.'.format(
                    usr=user.name),
                color=0xbf9626)
            bankteller.set_author(name='Automated Bank Teller System')
            bankteller.set_thumbnail(url='https://pays.host/uploads/bad83582-0b90-40ef-90f5-dd23b0ddbd42/T1cJqj6B.png')
            await user.send(embed=bankteller)

    async def generate_transaction(self, userid, type, amount, user):
        users = await self.get_bank_data()

        transid = token_hex()
        time = now.strftime("%H:%M:%S")
        date = today.strftime("%m/%d/%Y")

        users[userid.author.id]['transactions'].append({transid:{"type":type,"amount":amount,"date":date,"time":time,"payee":user}})

    async def check_if_exists(self, userid):
        users = await self.get_bank_data()
        if userid in users:
            return True
        else:
            return False


def setup(client):
    client.add_cog(Rewrite(client))
