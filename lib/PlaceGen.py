import random
import json

class Place:
    def __repr__(self):
        return f"Place(data={json.dumps(self.placeData, indent=2)})"

    def buildPlace(self):
        out = {}
        out['type'] = f"{random.choice(self.placeData['type'])} {random.choice(self.placeData['archetype'])}"
        
        return out

# class PlaceTemplate(Place):
#     placeData = {
#         'type': ['','','',''],
#         'archetype': ['','','','']
#     }

class CivSmall(Place):
    placeData = {
        'type': ['periphery','borderland','common','minor'],
        'archetype': ['barony','county','duchy','tribe']
    }

class CivLarge(Place):
    placeData = {
        'type': ['core','fallen','outsider','upstart'],
        'archetype': ['republic','kingdom','empire','horde']
    }

class Geo(Place):
    placeData = {
        'type': ['temperate','cold','desert','magical','small','vast','colorful','sky'],
        'archetype': ['coast','plain','forest','mountain','river','waterfall','overgrowth','plateau']
    }

class BuildingPoor(Place):
    placeData = {
        'type': ['produce','butcher','blacksmith','clothier','barber','mason'],
        'archetype': ['hovel','house','alley','dock']
    }

class BuildingRich(Place):
    placeData = {
        'type': ['jeweler','tavern','doctor','lawyer','engineer','admin'],
        'archetype': ['apartment','mansion','estate','park']
    }

class AncientRuins(Place):
    placeData = {
        'type': ['forgotten', 'crumbling', 'ruined'],
        'archetype': ['temple', 'citadel', 'palace']
    }

class EnchantedForest(Place):
    placeData = {
        'type': ['mystical', 'magical', 'enchanted'],
        'archetype': ['grove', 'glade', 'thicket']
    }

class PlaceCreator:
    def __init__(self, places=None):
        self.places = places if places is not None else Place.__subclasses__()

    def createPlaces(self, num=1):
        if num == 1:
            return random.choice(self.places)().buildPlace()
        out = {}
        for i in range(random.randint(1,num)):
            out[str(i)] = random.choice(self.places)().buildPlace()
        return out
