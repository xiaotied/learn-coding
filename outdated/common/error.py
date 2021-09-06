# coding: utf-8


class NoPathError(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message='need json format'):
        self.message = message


class NotFileError(Exception):
    def __init__(self, message='This is not a file'):
        self.message = message


class UserExistsError(Exception):
    def __init__(self, message):
        self.message = message


class RoleError(Exception):
    def __init__(self, message):
        self.message = message


class LevelError(Exception):
    def __init__(self, message):
        self.message = message


class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message


class NoUserError(Exception):
    def __init__(self, message):
        self.message = message


class UserActiveError(Exception):
    def __init__(self, message):
        self.message = message


class CountError(Exception):
    def __init__(self, message):
        self.message = message
