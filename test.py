import jsoneng
from lib import ApartmentBuildingSim, CharacterGenerator, FutureEventList

jdb = jsoneng.JsonDB()
jdb.create({})

human = CharacterGenerator.Human()
human.buildChar()

creator = CharacterGenerator.Create()
jdb.update(creator.createRoles())
