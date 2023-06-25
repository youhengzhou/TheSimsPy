import jsoneng
import os
import jsoneng

from lib import ApartmentBuildingSim, CharacterGenerator, FutureEventList

if __name__ == "__test__":
    startSimTime = int(os.environ.get("START_SIM_TIME"))
    endSimTime = int(os.environ.get("END_SIM_TIME"))
                                   
    jkdb = jsoneng.JsonDB()
    jdb.create({})

    human = CharacterGenerator.Human()
    human.buildChar()

    creator = CharacterGenerator.Create()
    jdb.update(creator.createRoles())
