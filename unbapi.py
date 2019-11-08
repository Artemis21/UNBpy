import requests
import json


API_VER = 'v1'


class APIError(Exception):
    '''
    An error for all non-200 API response codes.
    '''


class UNBUser:
    '''
    A class representing the data given by the API on a user. Contains cash, \
    bank, and rank data for a user. Also contains a guild and member object \
    for utility.
    '''
    def __init__(self, unbcl, guild, data):
        '''
        Internal (to the module) method - create the object.
        '''
        self.unbcl = unbcl
        self.guild = guild
        self.user = guild.get_member(data['user_id'])
        self.load(data)

    def load(self, data):
        '''
        Internal method - load raw json data.
        '''
        self.cash_ = data['cash']
        self.bank_ = data['bank']
        self.rank_ = data['rank']

    @property
    def cash(self): return self.cash_

    @cash.setter
    def cash(self, am, reason=''):
        self.load(self.unbcl.set_bal(self.user, am, False, reason))

    @property
    def bank(self): return self.bank_

    @bank.setter
    def bank(self, am, reason=''):
        self.load(self.unbcl.set_bal(self.user, am, True, reason))

    @property
    def total: return self.cash_ + self.bank_

    @property
    def rank: return self.rank_

    def reload(self):
        '''
        Reload the data, useful if it has changed by other means (eg. commands\
        ). This is automatically done after changing the cash or bank amounts.
        '''
        self.load(self.unbcl.get_user_data(self.user, self.guild))


class UNBClient:
    '''
    Client to send web requests to the UnbelievaBoat API.
    '''
    def __init__(self, token):
        '''
        Create client for connection with the API. Token can be obtained at \
        https://unbelievaboat.com/applications.
        '''
        self.url = 'https://unbelievaboat.com/api/' + API_VER
        self.auth = {
            'Authorization': token
        }

    def get_user_data(self, user, guild):
        '''
        Internal method - get raw json data for a user.
        '''
        url = f'{self.url}/guilds/{guild.id}/users/{user.id}'
        res = requests.get(url, headers=self.auth)
        if res.status != 200:
            raise APIError(res.json()['error'])
        return res.json()

    def set_bal(self, member, am, bank=True, reason=''):
        '''
        Internal method - set a user's balance.
        '''
        url = f'{self.url}/guilds/{member.guild.id}/users/{member.id}'
        data = json.dumps({
            ('cash', 'bank')[bank]: am,
            'reason': reason,
        })
        if res.status != 200:
            raise APIError(res.json()['error'])
        return res.json()

    def get_all_users(self, guild):
        '''
        Get every user in a guild, ordered by descending net worth.
        '''
        url = f'{self.url}/guilds/{guild.id}/users'
        res = requests.get(url, headers=self.auth)
        if res.status != 200:
            raise APIError(res.json()['error'])
        return [UNBUser(self, guild, i) for i in res.json()]

    def get_user(self, user, guild=None):
        '''
        Get a user by either a discord.py Member object or a discord.py User \
        object and a discord.py Guild object.
        '''
        guild = getattr(user, 'guild', guild)
        if not guild:
            raise TypeError(
                'Parameter user must be type Member if guild is not provided.'
            )
        return UNBUser(self, guild, self.get_user_data(user, guild))
