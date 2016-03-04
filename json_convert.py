import json

def explode_list(key, s_dict):
    ''' Run through a list piece by piece '''
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

# There are 3 files total with information in them.
# Load the file, convert to python data structures
# Close the file. 

unit_file = open('units.json', 'r')
unitdata = json.load(unit_file)
unit_file.close()

spell_ability_file = open('spellsAndAbilities.json', 'r')
sadata = json.load(spell_ability_file)
spell_ability_file.close()

dlc_file = open('dlc.json', 'r')
dlcdata = json.load(dlc_file)
dlc_file.close()


# Begin parsing out the dicts and nested structures to find the information we need.
# This is super basic at the moment, no formatting since I'm trying to figure out 
# how to pull and format properly in flat text.

full_unitdict = unitdata['WorldUnitTemplatesContainer']
unitdict = full_unitdict['unitsTemplates']
walldict = full_unitdict['wallsTemplates']

for item in unitdict['WorldUnitTemplate']:
    if item['race'] == 'HIGH_MEN':
        print('\n------START-----\n')
        for key in item:
            if isinstance(item[key], (list, dict)):
                explode_list(key, item[key])
            else:
                print(key + ' : ' + str(item[key]) + '\n')
        print('\n-----END-----')
