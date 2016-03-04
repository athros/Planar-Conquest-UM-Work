import json

def explode_list(key, s_dict):
    print('\n-----%s start-----' % key)   
    for k, v in s_dict.items():
        if isinstance(v, dict):
            #print(k + ' : ' + str(v))
            explode_list(k, v)
        elif isinstance(v, list):
            print('--%s start--' % k)
            print(k + ' : ' + str(v))
            print('--%s end--' % k)
        else:
            print(k + ' : ' + str(v))
    print('-----%s end-----\n' % key)

f = open('units.json', 'r')
jsondata = json.load(f)

d1 = jsondata['WorldUnitTemplatesContainer']
unitdict = d1['unitsTemplates']
walldict = d1['wallsTemplates']
del d1['unitsTemplates']
del d1['wallsTemplates']

for item in unitdict['WorldUnitTemplate']:
    if item['race'] == 'HIGH_MEN':
        print('\n------START-----\n')
        for key in item:
            if isinstance(item[key], (list, dict)):
                explode_list(key, item[key])
            else:
                print(key + ' : ' + str(item[key]) + '\n')
        print('\n-----END-----')
