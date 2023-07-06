import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

out = {
    "years": [
        {
            "year 1": {
                "important event": ["civil war", "drought"],
                "important civ": ["the rhodsions", "the egyptians"],
                "important people": ["john nolork", "casandra arnin"],
            },
        },
        {
            "year 2": {
                "important event": ["civil war", "drought"],
                "important civ": ["the rhodsions", "the egyptians"],
                "important people": ["zego novo", "khan novo"],
            },
        },
    ]
}

jdb.i(out)
