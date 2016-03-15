import random

RACES = ['High Men',
         'Unhallowed',
         'Gray Elves',
         'Dark Elves',
         'Dwarves',
         'Myrodants',
         'Orcs',
         'Draconians']

PLANES = ['Prime',
          'Water',
          'Fire',
          'Earth',
          'Air',
          'Paradise',
          'Shadow']

TYPE_OF_LANDMASS = ['Pangea',
                    'Two Contenints',
                    'Three Continents',
                    'Islands']

LANDMASS_PERCENTAGE = ['30%', '50%', '70%', '90%']

NUM_OF_PLANES = random.randint(1, 5)
PLANES_TO_PLAY = {}

RACE_TO_PLAY = RACES[random.randint(1, len(RACES)) - 1]

for i in range(1, NUM_OF_PLANES):
    plane = PLANES[random.randint(1, len(PLANES)) - 1]
    PLANES.remove(plane)
    landmass_type = TYPE_OF_LANDMASS[random.randint(1, len(TYPE_OF_LANDMASS)) - 1]
    landmass_percent = LANDMASS_PERCENTAGE[random.randint(1, len(LANDMASS_PERCENTAGE)) - 1]
    PLANES_TO_PLAY[plane] = "%s at %s" % (landmass_type, landmass_percent)

print 'Your Race is %s' % RACE_TO_PLAY
print'The chosen planes are: '
for pl in PLANES_TO_PLAY:
    print '\t%s with the options %s' % (pl, PLANES_TO_PLAY[pl])
