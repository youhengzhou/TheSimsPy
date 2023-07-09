import os
import jsoneng
import sys
from pathlib import Path

# sys.path.insert(0, '../lib')
# import CharGen

path_to_lib = Path(__file__).parent.parent / "lib"
sys.path.insert(0, str(path_to_lib.resolve()))
import CharGen, PlaceGen, RoleGen, FutureEventList

startSimTime = int(os.environ.get("START_SIM_TIME"))
endSimTime = int(os.environ.get("END_SIM_TIME"))

FutureEventList.run_simulation(startSimTime, endSimTime)

jdb = jsoneng.JsonDB()
jdb.create({})

human = CharGen.Human()
harry = human.buildChar("male")

print(harry)

charGen = CharGen.CharCreator()
placeGen = PlaceGen.PlaceCreator()
roleGen = RoleGen.RoleCreator()

jdb.p("chars", charGen.createChars())
jdb.p("roles", roleGen.createRoles())
jdb.p("places", placeGen.createPlaces(10))
