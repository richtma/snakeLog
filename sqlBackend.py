__author__ = 'core'

from sqlalchemy import Boolean, Column, create_engine, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///data/snakeLog.db', echo=True)

class DXCC(Base):
    __tablename__ = 'dxccs'

    _continent = Column(String(2))
    _cqzone = Column(Integer)
    _dxcc_id = Column(Integer, primary_key=True)
    _ituzone = Column(Integer)
    _latitude = Column(Float)
    _longitude = Column(Float)
    _name = Column(String)
    _prefixes = relationship("Prefix")
    _primaryprefix = relationship("Prefix", uselist=False)
    _timeoffset = Column(Float)

    def __init__(self):
        pass

    def __repr__(self):
        return "<DXCC('%s', '%s')>" % (self._primaryprefix, self._name)

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

class Prefix(Base):
    __tablename__ = 'prefixes'

    _override_cqzone = Column(Integer) #TODO: implementation
    _override_ituzone = Column(Integer) #TODO: implementation
    _prefix = Column(String, primary_key=True)
    _primary = Column(Boolean)

    _dxcc_id = Column(Integer, ForeignKey('dxccs._dxcc_id'))

    def __init__(self, prefix, isPrimary):
        self.set_prefix(prefix)
        self.set_primary(isPrimary)

    def __repr__(self):
        return "<Prefix('%s')>" % self._prefix

    def get_override_cqzone(self):
        return self._override_cqzone

    def set_override_cqzone(self, override_cqzone):
        self._timeoffset = override_cqzone

    def get_override_ituzone(self):
        return self._override_ituzone

    def set_override_ituzone(self, override_ituzone):
        self._timeoffset = override_ituzone

    def get_prefix(self):
        return self._prefix

    def set_prefix(self, prefix):
        self._prefix = prefix
        
    def get_primary(self):
        return self._primary
    
    def set_primary(self, primary):
        self._primary = primary
    

    override_cqzone = property(get_override_cqzone, set_override_cqzone)
    override_ituzone = property(get_override_ituzone, set_override_ituzone)
    prefix = property(get_prefix, set_prefix)
    primary = property(get_primary, set_primary)
    
    
class Qso:
    def __init__(self):
        pass

class Station:
    def __init__(self):
        pass


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class Database:
    def __init__(self):
        self.session = Session()

    def addDXCC(self, dxcc):
        self.session.add(dxcc)

    def commit(self):
        self.session.commit()

    def __del__(self):
        self.session.close()

