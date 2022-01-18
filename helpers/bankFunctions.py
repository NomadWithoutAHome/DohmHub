import json
import os
from secrets import token_hex
from datetime import datetime
from datetime import date
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/bankdb.json')

today = date.today()
now = datetime.now()

with open(my_file) as f:
    db = json.load(f)

class Economy(object):
    def __init__(self, account_name ):
        self.data = db
        self.accounts = db['Accounts']
        self.account_name = account_name


    def check_if_exists(self, userid):
        if userid in self.accounts:
            return True
        else:
            return False

    def open_account(self):
        self.accounts[self.account_name] = {"transactions":[]}
        self.accounts[self.account_name]['wallet'] = 1000
        self.accounts[self.account_name]['joindate'] = today.strftime("%m/%d/%Y")
        self.accounts[self.account_name]['hash'] = token_hex(5)

    def generate_transaction(self, type, amount, user):
        transid = token_hex()
        time = now.strftime("%H:%M:%S")
        date = today.strftime("%m/%d/%Y")

        self.accounts[self.account_name]['transactions'].append({transid:{"type":type,"amount":amount,"date":date,"time":time,"payee":user}})


    def save_account(self):
        datam = self.data
        with open(my_file, 'w+') as outfile:
            json.dump(datam, outfile)
        print('saving..')

    def delete_account(self):
        del self.accounts[self.account_name]

def load_database():
    with open(my_file) as f:
        db = json.load(f)
        return db


#test = Economy('dave')

#test.open_account()

#test.generate_transaction(type='payment', amount=200, user='nil')
#test.generate_transaction(type='payment', amount=20e0, user='nidl')
#test.save_account()