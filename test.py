import jsoneng
import os
import jsoneng

from lib import ApartmentBuildingSim, CharacterGenerator, FutureEventList

startSimTime = int(os.environ.get("START_SIM_TIME"))
endSimTime = int(os.environ.get("END_SIM_TIME"))

FutureEventList.run_simulation(startSimTime, endSimTime)

jdb = jsoneng.JsonDB()
jdb.create({})

human = CharacterGenerator.Human()
human.buildChar()

print(human)

creator = CharacterGenerator.Create()
jdb.update(creator.createRoles())
