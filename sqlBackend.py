__author__ = 'core'

import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("./data/snakeLog.sqlite")

    def addDXCC(self, dxcc):
        pass

class Qso:
    def __init__(self):
        pass

class Station:
    def __init__(self):
        pass

class DXCC:
    def __init__(self):
        pass

    name = property(get_name, set_name)
    cqzone = property(get_cqzone, set_cqzone)
    ituzone = property(get_ituzone, set_ituzone)
    continent = property(get_continent, set_continent)
    latitude = property(get_latitude, set_latitude)
    longitude = property(get_longitude, set_longitude)
    timeoffset = property(get_timeoffset, set_timeoffset)
    mainprefix = property(get_mainprefix, set_mainprefix)
    prefixes = property(get_prefixes, set_prefixes)