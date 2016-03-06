#!/usr/bin/env python3

import json

RACES = ['HIGH_MEN', 'UNHALLOWED', 'GRAY_ELVES', 'DARK_ELVES', 'DWARVES', 'INSECTOIDS', 'ORCS', 'DRACONIANS']
SUMMON_RACES = ['SUMMONS_DEATH', 'SUMMONS_EARTH', 'SUMMONS_AIR', 'SUMMONS_WATER', 'SUMMONS_FIRE', 'SUMMONS_LIFE']
OTHER_RACES = ['ANIMALS']
UNIT_TYPES = ['UNIT', 'SHIP', 'HERO', 'MONSTER', 'CHAMPION']

def explode_list(key, s_dict):
    ''' Run through a list/dict piece by piece '''
    print('\n-----%s start-----' % key)
    for k, v in s_dict.items():
        if isinstance(v, dict):
            #print(k + ' : ' + str(v))
            explode_list(k, v)
        # Tactical spells are under tacticalSpells/int 
        elif k == 'int':
            i = 0
            for spe in v:
                print(i, get_spell(spe))
                i = i + 1
        elif isinstance(v, list):
            print('--%s start--' % k)
            print(k + ' : ' + str(v))
            print('--%s end--' % k)
        else:
            print(k + ' : ' + str(v))
    print('-----%s end-----\n' % key)
    
def get_spell(id_num):
    '''Take in an id, output spell name'''
    spell = ''
    for sp in tactical_spells:
        if sp['id'] == str(id_num):
            spell = sp['spellName']
    return spell

################
# Script Start #
################

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

# Begin splitting out the dicts and nested structures into seperate 
# dicts for easier parsing.

# Units
full_unitdict = unitdata['WorldUnitTemplatesContainer']
unitdict = full_unitdict['unitsTemplates']
walldict = full_unitdict['wallsTemplates']

#Spells and Abilities
full_sa_dict = sadata['globalSpellbook']
strategic_abilities = full_sa_dict['strategicAbilities']
tactical_abilities = full_sa_dict['tacticalAbilities']
strategic_spells = full_sa_dict['strategicSpells']
tactical_spells = full_sa_dict['tacticalSpells']['tacticalSpell']
auras = full_sa_dict['auras']


###############
# Unit Parser #
###############

for race in RACES:
    for unit in unitdict['WorldUnitTemplate']:
        if unit['race'] == race:
            for unittype in UNIT_TYPES:
                if unittype == unit['battleStats']['type']:
                    print('\n#############################################')
                    print('# %s : %s : %s #' % (unit['race'], unit['battleStats']['name'], unit['battleStats']['type']))
                    print('#############################################')
                    print('#\t\tStarting Stats\t\t#')
                    print('------------------------------')
                    print('#\tSTR: %s\t#\tINT: %s\t#' % (unit['battleStats']['abilityScores']['strength']['score'],
                                                        unit['battleStats']['abilityScores']['intellegence']['score']))
                    print('#\tDEX: %s\t#\tWIS: %s\t#' % (unit['battleStats']['abilityScores']['dexterity']['score'],
                                                        unit['battleStats']['abilityScores']['wisdom']['score']))
                    print('#\tCON: %s\t#\tCHA: %s\t#' % (unit['battleStats']['abilityScores']['constitution']['score'],
                                                        unit['battleStats']['abilityScores']['charisma']['score']))
                    print('##############################')
                    print('#\t\t\tSpells\t\t\t#')
                    print('-------------------------')
                    try:
                        tac_spells = unit['battleStats']['tacticalSpells']['int']
                        for s in tac_spells:
                            print('#\t%s' % (get_spell(s)))
                    except KeyError:
                        print('#\t\tNo Spells\t\t\t#')
                    print('##############################')