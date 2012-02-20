__author__ = 'core'

# http://www.country-files.com/cty/format.htm

from sqlBackend import DXCC

from string import find, split, strip

class CountryImporter:
    def __init__(self, file):
        self.file = file

    def importCountrys(self, db):
        cty = open("data/cty.dat", 'r')

        information = []
        prefixes = []
        EOEtoggle = False
        for line in cty:
            data = split(line, ":")
            data = map(lambda x: strip(x), data)

            if EOEtoggle:
                EOEtoggle = False
                country = DXCC()
                country['name'] = information[0]
                country['cqzone'] = information[1]
                country['ituzone'] = information[2]
                country['continent'] = information[3]
                country['latitude'] = information[4]
                country['longitude'] = information[5]
                country['timeoffset'] = information[6]
                country['primaryprefix'] = information[7]
                country['prefixes'] = prefixes
                db.addDXCC(country)
                information = []
                prefixes = []

            if len(data) == 1:
                if find(data[0], ";") != -1:
                    EOEtoggle = True
                prefixes += split(strip(data[0], ";"), ",")[:-1]
            else:
                information = data

        cty.close()