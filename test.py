import os
import jsoneng

from lib import ApartmentBuildingSim, CharGen, PlaceGen, RoleGen, FutureEventList

startSimTime = int(os.environ.get("START_SIM_TIME"))
endSimTime = int(os.environ.get("END_SIM_TIME"))

FutureEventList.run_simulation(startSimTime, endSimTime)

jdb = jsoneng.JsonDB()
jdb.create({})

human = CharGen.Human()
harry = human.buildChar('male')

print(harry)

charGen = CharGen.CharCreator()
placeGen = PlaceGen.PlaceCreator()
roleGen = RoleGen.RoleCreator()

jdb.p('chars',charGen.createChars())
jdb.p('roles',roleGen.createRoles())
jdb.p('places',placeGen.createPlaces(10))
