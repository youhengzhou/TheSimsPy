import random
import json

class Char:
    def __repr__(self):
        return f"Char(data={json.dumps(self.charData, indent=2)})"
    
    def buildChar(self):
        out = {}
        out['type'] = f"{random.choice(self.charData['type'])} {random.choice(self.charData['gender'])} {random.choice(self.charData['name'])}"
        out['look'] = f"{random.choice(self.charData['look'])} {random.choice(self.charData['build'])} {random.choice(self.charData['style'])}"
        out['skill'] = random.choice(self.charData['skill'])
        return out
    
class Human(Char):
    charData = {
        'type':
        ['lyonian','falconian','borderlander','draconian','tigian'],
        'gender': ['male','female'],
        'name':
        ['common','archaic','uncommon','noble'],
        'look':
        ['plain','soft','attractive','stern'],
        'build':
        ['normal','small','muscular','lean'],
        'style':
        ['incognito','simple','stylish','heavy'],
        'skill':
        ['diplomacy','martial','subterfuge','learning']
    }

class Dragon(Char):
    charData = {
        'type':
        ['frost','water','fire','desert'],
        'gender': ['male','female'],
        'name':
        ['common','archaic','uncommon','noble'],
        'look':
        ['rough','smooth','horned','scaled'],
        'build':
        ['normal','light','giant','long'],
        'style':
        ['draconic'],
        'skill':
        ['fire breathing']
    }

class Dwarf(Char):
    charData = {
        'type': 
        ['mountain', 'hill', 'cave'],
        'gender': 
        ['male', 'female'],
        'name': 
        ['common', 'archaic', 'uncommon', 'noble'],
        'look': 
        ['stout', 'strong', 'bearded'],
        'build': 
        ['stocky', 'muscular', 'athletic'],
        'style': 
        ['practical', 'rugged', 'traditional'],
        'skill': 
        ['mining', 'crafting', 'combat']
    }

class Elf(Char):
    charData = {
        'type': 
        ['lyonian', 'frost', 'desert'],
        'gender': 
        ['male', 'female'],
        'name': 
        ['common', 'archaic', 'uncommon', 'noble'],
        'look': 
        ['plain', 'soft', 'attractive', 'stern'],
        'build': 
        ['normal', 'small', 'muscular', 'lean'],
        'style': 
        ['incognito', 'simple', 'stylish', 'heavy'],
        'skill': 
        ['diplomacy', 'martial', 'subterfuge', 'learning', 'magic', 'arcane']
    }

class Orc(Char):
    charData = {
        'type': 
        ['savage', 'warrior', 'shaman'],
        'gender': 
        ['male', 'female'],
        'name': 
        ['common', 'archaic', 'uncommon', 'noble'],
        'look': 
        ['ferocious', 'intimidating', 'tattooed'],
        'build': 
        ['brawny', 'muscular', 'hulking'],
        'style': 
        ['barbaric', 'tribal', 'battle-hardened'],
        'skill': 
        ['combat', 'survival', 'brute strength']
    }

class Vampire(Char):
    charData = {
        'type': 
        ['classic', 'seductive', 'feral'],
        'gender': 
        ['male', 'female'],
        'name': 
        ['common', 'archaic', 'elegant', 'noble'],
        'look': 
        ['pale', 'mesmerizing', 'mysterious'],
        'build': 
        ['slender', 'lithe', 'graceful'],
        'style': 
        ['elegant', 'gothic', 'modern'],
        'skill': 
        ['seduction', 'hypnosis', 'immortality'],
    }

class Role:
    def __repr__(self):
        return f"Role(data={json.dumps(self.roleData, indent=2)})"
    
    def buildRole(self):
        out = {}
        out['type'] = self.roleData['type']
        out['archetype'] = random.choice(self.roleData['archetype'])
        for years in range(random.randint(1,4)):
            event = random.choice(list(self.roleData['events'].keys()))
            out[event] = random.choice(self.roleData['events'][event])
        if years >= 2:
            out['reward'] = random.choice(self.roleData['rewards'])
        return out

class RoleTemplate(Role):
    roleData = {
        'type': '',
        'archetype':
        ['','','',''],
        'events':
        {'': ['',''],
        '': ['','']},
        'rewards': ['','','']
    }

class Place:
    def __repr__(self):
        return f"Place(data={json.dumps(self.placeData, indent=2)})"

    def buildPlace(self):
        out = {}
        out['type'] = f"{random.choice(self.placeData['type'])} {random.choice(self.placeData['archetype'])}"
        
        return out

class PlaceTemplate(Place):
    placeData = {
        'type': ['','','',''],
        'archetype': ['','','','']
    }

class Soldier(Role):
    roleData = {
        'type': 'soldier',
        'archetype':
        ['infantry','skirmisher','cavalry','frontier guard'],
        'events':
        {'sacking': ['avoid','partake'],
        'smuggling': ['denounce','partake'],
        'outnumbered': ['last stand','tactical decision'],
        'skirmish': ['repel','fall back'],
        'pitch battle': ['reward','scarred']},
        'rewards': ['brothers-in-arms','survival','weapon proficiency']
    }

class Mercenary(Role):
    roleData = {
        'type': 'mercenary',
        'archetype':
        ['great company','tigian golden arms','falconian holy knights','black boars'],
        'events':
        {'downtime': ['new friends','new vices'],
        'changing side': ['tigian empire','draconian tribes'],
        'outnumbered': ['last stand','tactical decision'],
        'skirmish': ['repel','fall back'],
        'pitch battle': ['reward','scarred']},
        'rewards': ['riches','concubines','stallion']
    }

class Pilgrim(Role):
    roleData = {
        'type': 'pilgrim',
        'archetype':
        ['falconian coast','lyonian tundra','borderland mountains','tigian sands'],
        'events':
        {'dark place': ['forgotten temple','monster cavern'],
        'campfire': ['share with others','join with others']},
        'rewards': ['wild medicine','divine protection','tireless walker']
    }

class Monk(Role):
    roleData = {
        'type': 'monk',
        'archetype':
        ['redemption','spirituality','misanthropy','knowledge'],
        'events':
        {'mentor': ['life wisdom','scientific knowledge'],
        'studies': ['gain faith','gain doubts']},
        'rewards': ['great archives','guided trance','fortified mind']
    }

class Priest(Role):
    roleData = {
        'type': 'priest',
        'archetype':
        ['local','imperial','lyonian orthodoxy','tigian orthodoxy'],
        'events':
        {'plague': ['welcomed','sent away'],
        'temptress': ['rejected','sinned']},
        'rewards': ['cult following','cardinal','crazed nun']
    }

class Citizen(Role):
    roleData = {
        'type': 'citizen',
        'archetype':
        ['shop','service','inn','worker'],
        'events':
        {'profits': ['new fortune','new connections'],
        'pickpocket': ['alms','called guards']},
        'rewards': ['expansion','friends in high places','passive income']
    }

class Thug(Role):
    roleData = {
        'type': 'thug',
        'archetype':
        ['ivory fangs','the spankers','mad bastards','smiling fellas'],
        'events':
        {'extorsion': ['grieving widow','rich merchant'],
        'stealing whores': ['snitched','took a cut']},
        'rewards': ['pimp','your own band','right hand man']
    }

class BallRoomRogue(Role):
    roleData = {
        'type': 'ballroom rogue',
        'archetypes': ['falconian balls','lyonian heaths','tigian parades','borderland courts'],
        'events':
        {'paramour': ['young princess','queen mother'],
         'take cut': ['priceless jewels','gold coins']},
         'rewards': ['title','estate','forbidden knowledge']
    }

class Wizard(Role):
    roleData = {
        'type': 'wizard',
        'archetype': ['elementalist', 'enchanter', 'necromancer', 'illusionist'],
        'events': {
            'apprenticeship': ['wise master', 'rivalry'],
            'arcane experiment': ['success', 'disaster'],
            'forbidden knowledge': ['embrace', 'reject']
        },
        'rewards': ['spellbook', 'familiar', 'arcane artifact']
    }

class Assassin(Role):
    roleData = {
        'type': 'assassin',
        'archetype': ['silent blade', 'poisoner', 'shadow dancer', 'contract killer'],
        'events': {
            'training': ['master assassin', 'rivalry'],
            'target elimination': ['successful', 'failed'],
            'betrayal': ['loyal', 'double-cross']
        },
        'rewards': ['secrets', 'hidden resources', 'legendary weapon']
    }

class Noble(Role):
    roleData = {
        'type': 'noble',
        'archetype': ['king', 'queen', 'duke', 'duchess'],
        'events': {
            'inheritance': ['wealth', 'debt'],
            'political intrigue': ['manipulate', 'betray'],
            'court scandal': ['survive', 'exile']
        },
        'rewards': ['power', 'prestige', 'land']
    }

class Bard(Role):
    roleData = {
        'type': 'bard',
        'archetype': ['troubadour', 'minstrel', 'jester', 'skald'],
        'events': {
            'musical apprenticeship': ['masterful mentor', 'rivalry'],
            'performance success': ['adored by audience', 'heckled off stage'],
            'bardic tale': ['legendary ballad', 'forgotten verse']
        },
        'rewards': ['fame', 'inspiration', 'musical instrument']
    }

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

class Create:
    def __init__(self, chars=[], roles=[], places=[]):
        if not chars:
            self.chars = Char.__subclasses__()
        else:
            self.chars = chars
        if not roles:
            self.roles = Role.__subclasses__()
        else:
            self.roles = roles
        if not places:
            self.places = Place.__subclasses__()
        else:
            self.places = places

    def createChars(self):
        out = {}
        for i in range(random.randint(4,4)):
            out[str(i)] = random.choice(self.chars)().buildChar()
        return out

    def createRoles(self):
        out = {}
        for i in range(random.randint(4,4)):
            c = Human().buildChar()
            c['history'] = random.choice(self.roles)().buildRole()
            out[i] = c
        return out
    
    def createPlaces(self):
        out = {}
        for i in range(random.randint(4,4)):
            out[str(i)] = random.choice(self.places)().buildPlace()
        return out
