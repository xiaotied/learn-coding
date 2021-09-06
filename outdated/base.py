# coding: utf-8

import os
import json
import time

from common.utils import check_file, timestamp_to_str
from common.error import (UserExistsError, RoleError,
                          LevelError, NegativeNumberError, CountError)
from common.consts import ROLES, FIRSTLEVELS, SECONDLEVELS


class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()
        self.__init_gifts()

    def __check_user_json(self):
        check_file(self.user_json)

    def __check_gift_json(self):
        check_file(self.gift_json)

    def __read_users(self, time_to_str=False):
        with open(self.user_json, 'r') as f:
            data = json.loads(f.read())

        if time_to_str == True:
            for username, v in data.items():
                v['create_time'] = timestamp_to_str(v['create_time'])
                v['update_time'] = timestamp_to_str(v['update_time'])
                data[username] = v

        return data

    def __write_user(self, **user):
        if 'username' not in user:
            raise ValueError('Missing username')
        if 'role' not in user:
            raise ValueError('Missing role')

        user['active'] = True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []

        users = self.__read_users()

        if user['username'] in users:
            raise UserExistsError('username %s had exists' % user['username'])

        users.update(
            {user['username']: user}
        )

        self.__save(users, self.user_json)

    def __change_role(self, username, role):
        users = self.__read_users()
        user = users.get(username)  # {'username':{role, create_time}}
        if not user:
            return False

        if role not in ROLES:
            raise RoleError('Invalid role: %s' % role)

        user['role'] = role
        user['update_time'] = time.time()
        users[username] = user

        self.__save(users, self.user_json)
        return True

    def __change_active(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user

        self.__save(users, self.user_json)
        return True

    def __delete_user(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        delete_user = users.pop(username)
        self.__save(users, self.user_json)
        return delete_user

    def __read_gifts(self):
        with open(self.gift_json) as f:
            data = json.loads(f.read())
        return data

    def __init_gifts(self):
        data = {
            'level1': {
                'level1': {},
                'level2': {},
                'level3': {},
            },
            'level2': {
                'level1': {},
                'level2': {},
                'level3': {},
            },
            'level3': {
                'level1': {},
                'level2': {},
                'level3': {},
            },
            'level4': {
                'level1': {},
                'level2': {},
                'level3': {},
            }
        }
        gifts = self.__read_gifts()
        if len(gifts) != 0:
            return

        self.__save(data, self.gift_json)

    def __write_gift(self, first_level, second_level, gift_name, gift_count):

        if first_level not in FIRSTLEVELS:
            raise LevelError('First level is not exists.')
        if second_level not in SECONDLEVELS:
            raise LevelError('Second level is not exists.')

        gifts = self.__read_gifts()

        current_gift_poll = gifts[first_level]
        current_second_gift_poll = current_gift_poll[second_level]

        if gift_count <= 0:
            gift_count = 1

        if gift_name in current_second_gift_poll:
            current_second_gift_poll[gift_name]['count'] = current_second_gift_poll[gift_name]['count'] + gift_count
        else:
            current_second_gift_poll[gift_name] = {
                'name': gift_name,
                'count': gift_count
            }

        current_gift_poll[second_level] = current_second_gift_poll
        gifts[first_level] = current_gift_poll
        self.__save(gifts, self.gift_json)

    def __update_gift(self, first_level, second_level,
                      gift_name, gift_count=1, is_admin=False):
        assert isinstance(gift_count, int), 'Gift count is a integer.'
        data = self.__check_get_gift(first_level, second_level, gift_name)

        if data == False:
            return data

        current_gift_poll = data.get('level_one')
        current_second_gift_poll = data.get('level_two')
        gifts = data.get('gifts')

        current_gift = current_second_gift_poll[gift_name]

        if is_admin == True:
            if gift_count <= 0:
                raise CountError('Gift count cannot be zero.')

            current_gift['count'] = gift_count

        else:
            if current_gift['count'] - gift_count < 0:
                raise NegativeNumberError('Gift count cannot be negative.')

            current_gift['count'] -= gift_count

        current_second_gift_poll[gift_name] = current_gift
        current_gift_poll[second_level] = current_second_gift_poll
        gifts[first_level] = current_gift_poll

        self.__save(gifts, self.gift_json)

    def __check_get_gift(self, first_level, second_level, gift_name):
        if first_level not in FIRSTLEVELS:
            raise LevelError('First level is not exists.')
        if second_level not in SECONDLEVELS:
            raise LevelError('Second level is not exists.')

        gifts = self.__read_gifts()

        level_one = gifts[first_level]
        level_two = level_one[second_level]

        if gift_name not in level_two:
            return False

        return {
            'level_one': level_one,
            'level_two': level_two,
            'gifts': gifts
        }

    def __delete_gift(self, first_level, second_level, gift_name):
        data = self.__check_get_gift(first_level, second_level, gift_name)

        if data == False:
            return data

        current_gift_poll = data.get('level_one')
        current_second_gift_poll = data.get('level_two')
        gifts = data.get('gifts')

        delete_gift_data = current_second_gift_poll.pop(gift_name)
        current_gift_poll[second_level] = current_second_gift_poll
        gifts[first_level] = current_gift_poll

        self.__save(gifts, self.gift_json)
        return delete_gift_data

    def __save(self, data, path):
        json_data = json.dumps(data)
        with open(path, 'w') as f:
            f.write(json_data)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    print(gift_path)
    print(user_path)
    base = Base(user_json=user_path, gift_json=gift_path)

    # base.write_user(username='peter', role='admin')

    base.delete_gift(first_level='level4', second_level='level3', gift_name='$55000')
    # print(result)
