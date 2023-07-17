import jsoneng

jdb = jsoneng.JsonDB()

d = jdb.retrieve("TYOV")

o = []

for k in d:
    if len(d[k]) > 2:
        o.append(k)
        # print(d[k])

jdb.c(1,o,'tochange')
