guardEncounter = """
you stumbled onto some guards in the place, roll to determine

roll d4
>4: you are safe
3: the guards saw you but not your face
check speed >4 to escape
2: the guards stops you for a routine inspection
check sanity >4 to escape
1: the guards saw you and your face
check speed >4 to escape, the guards are on high alert now
0: the guards stops you and initiate combat
create 1 to 4 guards as enemy
"""

events = [guardEncounter]

wraithInTheMirror = """
the player next to you saw a wraith in the mirror
it is their future self, and in order to help them
they must discard one item to the mirror
"""

omens = [wraithInTheMirror]

forgery = """
forging papers or documents for a new identity can be useful
for infiltrating certain guarded places

there are a few ways you can forge identities

MASTER FORGER
a master forger can forget identities for you,
but they become increasingly expensive the more you
come to them, as the officials become more vigiliant

1st time, 1 wealth
2nd time, 2 wealth
3rd time, 4 wealth... and so on

GANG
a local gang offers to forge you a new set of identities
in exchange, you help the gang take out some rivals
due to the heat from local authorities, the gang can
only do this for 3 times

each time, take out target of grit 6, speed 6
"""

investigate = """
the investigation action helps you uncover knowledge
you did not know before

there are a few types of investiations

ARCHIVAL
you chose to investigate information using archives,
newspapers, and other written forms of media, following
the paper trail to your destination

roll knowledge
>4: get some information
<4: get half truths
<0: failed to get information

PEOPLE
you chose to investigate the good old fashioned why,
conducting interviews on the streets with witnesses,
and other seedy individuals, perhaps through bribes
or other nefarious means

roll sanity
>4: get some information
<4: get half truths
<0: failed to get information
"""

actions = [forgery, investigate]
