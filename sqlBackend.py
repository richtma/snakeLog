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

    def get_continent(self):
        return self._continent

    def set_continent(self, continent):
        self._continent = continent

    def get_cqzone(self):
        return self._cqzone

    def set_cqzone(self, cqzone):
        self._cqzone = cqzone

    def get_ituzone(self):
        return self._ituzone

    def set_ituzone(self, ituzone):
        self._ituzone = ituzone

    def get_latitude(self):
        return self._latitude

    def set_latitude(self, latitude):
        self._latitude = latitude

    def get_longitude(self):
        return self._longitude

    def set_longitude(self, longitude):
        self._longitude = longitude

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_prefixes(self):
        return self._prefixes

    def set_prefixes(self, prefixes):
        self._prefixes = prefixes

    def get_primaryprefix(self):
        return self._primaryprefix

    def set_primaryprefix(self, primaryprefix):
        self._primaryprefix = primaryprefix

    def get_timeoffset(self):
        return self._timeoffset

    def set_timeoffset(self, timeoffset):
        self._timeoffset = timeoffset

    continent = property(get_continent, set_continent)
    cqzone = property(get_cqzone, set_cqzone)
    ituzone = property(get_ituzone, set_ituzone)
    latitude = property(get_latitude, set_latitude)
    longitude = property(get_longitude, set_longitude)
    name = property(get_name, set_name)
    prefixes = property(get_prefixes, set_prefixes)
    primaryprefix = property(get_primaryprefix, set_primaryprefix)
    timeoffset = property(get_timeoffset, set_timeoffset)