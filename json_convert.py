#!/usr/bin/env python3

import json
import re

RACES = ['HIGH_MEN',
         'UNHALLOWED',
         'GRAY_ELVES',
         'DARK_ELVES',
         'DWARVES',
         'INSECTOIDS',
         'ORCS',
         'DRACONIANS']

SUMMON_RACES = ['SUMMONS_DEATH',
                'SUMMONS_EARTH',
                'SUMMONS_AIR',
                'SUMMONS_WATER',
                'SUMMONS_FIRE',
                'SUMMONS_LIFE']

UNIT_TYPES = ['UNIT',
              'SHIP',
              'HERO',
              'MONSTER',
              'CHAMPION']

OTHER_RACES = ['ANIMALS']

RANGED_RE = re.compile('[Rr]anged.*$')


def explode_list(key, s_dict):
    ''' Run through a list/dict piece by piece '''
    print('\n-----%s start-----' % key)
    for k, v in s_dict.items():
        if isinstance(v, dict):
            print('DICT\n')
            explode_list(k, v)
        # Tactical spells are under tacticalSpells/int
        elif k == 'int':
            i = 0
            for spe in v:
                print(i, get_tspell(spe))
                i = i + 1
        elif isinstance(v, list):
            print('LIST\n')
            print('--%s start--' % k)
            print(k + ' : ' + str(v))
            print('--%s end--' % k)
        else:
            print(k + ' : ' + str(v))
    print('-----%s end-----\n' % key)


def get_tspell(id_num):
    '''Take in an id, output spell name'''
    spell = ''
    for sp in tactical_spells:
        if sp['id'] == str(id_num):
            spell = sp['spellName']
    return spell


def get_sability(id_num):
    '''Take in an id, output spell name'''
    sability = ''
    for sa in strategic_abilities:
        if sa['ID'] == str(id_num):
            sability = sa['name']
    return sability


def stats_display(ud):
    print('#\t\tStarting Stats\t\t#')
    print('------------------------------')
    print('#\tSTR: %s\t#\tINT: %s\t#' %
          (unit['battleStats']['abilityScores']['strength']['score'],
           unit['battleStats']['abilityScores']['intellegence']['score']))
    print('#\tDEX: %s\t#\tWIS: %s\t#' %
          (unit['battleStats']['abilityScores']['dexterity']['score'],
           unit['battleStats']['abilityScores']['wisdom']['score']))
    print('#\tCON: %s\t#\tCHA: %s\t#' %
          (unit['battleStats']['abilityScores']['constitution']['score'],
           unit['battleStats']['abilityScores']['charisma']['score']))
    print('##############################')


def tac_spells_display(ud):
    print('#\tTactical Spells\t\t#')
    print('-------------------------')
    try:
        tac_spells = ud['battleStats']['tacticalSpells']['int']
        for s in tac_spells:
            print('#\t%s' % (get_tspell(s)))
    except KeyError:
        print('#\t\tNo Spells\t\t\t#')
    print('##############################')


def strat_abilities_display(ud):
    print('#\tStrategic Map Abilities\t\t#')
    print('-------------------------')
    try:
        sabilitys = unit['battleStats']['strategicAbilities']['int']
        for s in sabilitys:
            print('#\t%s' % (get_sability(s)))
    except KeyError:
        print('#\tNo Strategic Abilities\t\t#')
    print('##############################')


def upkeep_display(ud):
    print('#\tUpkeep Costs\t\t\t#')
    print('-------------------------')
    if int(ud['foodUpkeepCost']) > 0:
        print('#\t Food Upkeep: %s\t\t\t\t#' % (ud['foodUpkeepCost']))
    if int(ud['goldUpkeepCost']) > 0:
        print('#\t Gold Upkeep: %s\t\t\t\t#' % (ud['goldUpkeepCost']))
    if int(ud['manaUpkeepCost']) > 0:
        print('#\t Mana Upkeep: %s\t\t\t\t#' % (ud['manaUpkeepCost']))
    if int(ud['neUpkeepCost']) > 0:
        print('#\t Negative Energy Upkeep: %s\t#' % (ud['neUpkeepCost']))


def attack_display(ud):
    print('#\t\tAttacks\t\t\t#')
    try:
        atk_type = type(ud['battleStats']['attacks']['Attack'])
        if atk_type is list:
            i = 1
            for atk in ud['battleStats']['attacks']['Attack']:
                print('#########################################')
                print('#\t\tAttack Number %i\t\t#' % i)
                print('#########################################')
                print('#\tAttack Type: %s\t#' % (atk['attackType']))
                print('#\tAttack Bonus: %s\t\t#' %
                      atk['additionalAttackBonus'])
                print('#\tCritical Range: %s\t\t#' % atk['criticalRange'])
                print('#\tCritical Multiplier: %s\t\t#' %
                      atk['criticalMultiplier'])
                if re.match(RANGED_RE, atk['attackType']):
                    print('#\tRange Increment: %s\t\t#' %
                          atk['rangeIncrement'])
                print('##\tDamage\t\t\t\t#')
                print('#\tWeapon Type: %s\t\t#' %
                      atk['diceList']['DamageDie']['weaponType'])
                print('#\tDamage Type: %s\t\t#' %
                      atk['diceList']['DamageDie']['damageType'])
                print('#\tDamage Dice: %sd%s\t\t#' %
                      (atk['diceList']['DamageDie']['count'],
                       atk['diceList']['DamageDie']['dieType']))
                print('#\tDamage Bonus: %s\t\t\t#' %
                      atk['diceList']['DamageDie']['addAttackDamageBonus'])
                for k, v in atk.items():
                    print(k, v)
                print('#########################################')
                i += 1
        elif atk_type is dict:
            atk = ud['battleStats']['attacks']['Attack']
            print('#########################################')
            print('#\t\tAttack\t\t#')
            print('#########################################')
            print('#\tAttack Type: %s\t#' % atk['attackType'])
            print('#\tAttack Bonus: %s\t\t#' % atk['additionalAttackBonus'])
            print('#\tCritical Range: %s\t\t#' % atk['criticalRange'])
            print('#\tCritical Multiplier: %s\t\t#' %
                  atk['criticalMultiplier'])
            if re.match(RANGED_RE, atk['attackType']):
                print('#\tRange Increment: %s\t\t#' %
                      atk['rangeIncrement'])
            print('##\tDamage\t\t\t\t#')
            print('#\tWeapon Type: %s\t\t#' %
                  atk['diceList']['DamageDie']['weaponType'])
            print('#\tDamage Type: %s\t\t#' %
                  atk['diceList']['DamageDie']['damageType'])
            print('#\tDamage Dice: %sd%s\t\t#' %
                  (atk['diceList']['DamageDie']['count'],
                   atk['diceList']['DamageDie']['dieType']))
            print('#\tDamage Bonus: %s\t\t\t#' %
                  atk['diceList']['DamageDie']['addAttackDamageBonus'])
            print('#########################################')
#    except Exception as inst:
#        print(type(inst))    # the exception instance
#        print(inst.args)     # arguments stored in .args
#        print(inst)
    except:
        print('#\t\tNo Attacks\t\t#')

################
# Script Start #
################

# There are 3 files total with information in them.
# Load the file, convert to python data structures
# Close the file.

unit_file = open('./data/units.json', 'r')
unitdata = json.load(unit_file)
unit_file.close()

spell_ability_file = open('./data/spellsAndAbilities.json', 'r')
sadata = json.load(spell_ability_file)
spell_ability_file.close()

dlc_file = open('./data/dlc.json', 'r')
dlcdata = json.load(dlc_file)
dlc_file.close()

# Begin splitting out the dicts and nested structures into seperate
# dicts for easier parsing.

# Units
full_unitdict = unitdata['WorldUnitTemplatesContainer']
unitdict = full_unitdict['unitsTemplates']
walldict = full_unitdict['wallsTemplates']

# Spells and Abilities
full_sa_dict = sadata['globalSpellbook']
strategic_abilities = full_sa_dict['strategicAbilities']['strategicAbility']
tactical_abilities = full_sa_dict['tacticalAbilities']
strategic_spells = full_sa_dict['strategicSpells']
tactical_spells = full_sa_dict['tacticalSpells']['tacticalSpell']
auras = full_sa_dict['auras']

# DLC Stuff
full_dlc_dict = dlcdata['HiddenXMLContainer']
dlc_units = full_dlc_dict['dlcUnits']
dlc_lords = full_dlc_dict['dlcLords']
dlc_items = full_dlc_dict['dlcItems']
ai_cheats = full_dlc_dict['aiCheats']

###############
# Unit Parser #
###############

for race in RACES:
    print('\n\n#############################################')
    print('%s' % str(race))
    print('#############################################\n')
    for unit in unitdict['WorldUnitTemplate']:
        if unit['race'] == race:
            for unittype in UNIT_TYPES:
                if unittype == unit['battleStats']['type']:
                    print('\n#############################################')
                    print('# %s : %s : %s #' % (unit['race'],
                                                unit['battleStats']['name'],
                                                unit['battleStats']['type']))
                    print('#############################################')
                    stats_display(unit)
                    tac_spells_display(unit)
                    strat_abilities_display(unit)
                    upkeep_display(unit)
                    attack_display(unit)
                    print('#############################################\n')
