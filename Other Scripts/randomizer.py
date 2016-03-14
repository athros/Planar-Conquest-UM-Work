import random

PLANES = ['Prime', 'Water', 'Fire', 'Earth', 'Air', 'Paradise', 'Shadow']

TYPE_OF_LANDMASS = ['Pangea', 'Two Contenints', 'Three Continents', 'Islands']
LANDMASS_PERCENTAGE = ['30%', '50%', '70%', '90%']

NUM_OF_PLANES = random.randint(1, 5)
PLANES_TO_PLAY = {}

for i in range(1, NUM_OF_PLANES):
    plane = PLANES[random.randint(1, len(PLANES)) - 1]
    PLANES.remove(plane)
    landmass_type = TYPE_OF_LANDMASS[random.randint(1, len(TYPE_OF_LANDMASS)) - 1]
    landmass_percent = LANDMASS_PERCENTAGE[random.randint(1, len(LANDMASS_PERCENTAGE)) - 1]
    PLANES_TO_PLAY[plane] = "%s at %s" % (landmass_type, landmass_percent)
    
print(PLANES_TO_PLAY)