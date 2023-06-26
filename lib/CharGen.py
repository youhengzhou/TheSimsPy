import random
import json

class Char:
    def __repr__(self):
        return f"Char(data={json.dumps(self.charData, indent=2)})"
    
    def buildChar(self, gender=''):
        if not gender:
            gender = random.choice(self.charData['gender'])
        out = {}
        out['type'] = f"{random.choice(self.charData['type'])} {gender} {random.choice(self.charData['name'])}"
        out['look'] = f"{random.choice(self.charData['look'])} {random.choice(self.charData['build'])} {random.choice(self.charData['style'])}"
        out['skill'] = random.choice(self.charData['skill'])
        return out

# class CharTemplate(Char):
#     charData = {
#         'type':
#         [''],
#         'gender': [''],
#         'name':
#         [''],
#         'look':
#         [''],
#         'build':
#         [''],
#         'style':
#         [''],
#         'skill':
#         [''],
#     }
    
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

class CharCreator:
    def __init__(self, chars=[]):
        if not chars:
            self.chars = Char.__subclasses__()
        else:
            self.chars = chars

    def createChars(self, num=1):
        out = {}
        if num == 1:
            return random.choice(self.chars)().buildChar()
        for i in range(random.randint(1,num)):
            out[str(i)] = random.choice(self.chars)().buildChar()
        return out
