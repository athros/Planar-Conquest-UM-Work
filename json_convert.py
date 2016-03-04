import json

f = open('units.json', 'r')
jsondata = json.load(f)

d1 = jsondata['WorldUnitTemplatesContainer']
unitdict = d1['unitsTemplates']
walldict = d1['wallsTemplates']
del d1['unitsTemplates']
del d1['wallsTemplates']

print(d1)
for item in unitdict['WorldUnitTemplate']:
    if item['race'] == 'HIGH_MEN':
        print('\n------START-----\n')
        for key in item:
            print(key + ' : ' + str(item[key]) + '\n')
        print('\n-----END-----')
#print(unitdict)
print('\n\n\n')
#print(walldict)
