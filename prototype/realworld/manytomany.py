from dataclasses import dataclass, field, asdict
from typing import Dict

import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


@dataclass
class Test:
    thing: list


a = Test([1, 2, 3])
a.thing2 = [1, 2, 3]

b = Test([1, 2, 3])

thing = [] if b.thing2 is None else b.thing2
print(thing)

# @dataclass
# class A:
#     name: str
#     bs: Dict[str, "B"] = field(default_factory=dict)

#     def add_b(self, b: "B"):
#         self.bs[b.name] = b


# @dataclass
# class B:
#     name: str
#     as_: Dict[str, A] = field(default_factory=dict)

#     def add_a(self, a: A):
#         self.as_[a.name] = a


# a1 = A("A1")
# a2 = A("A2")
# b1 = B("B1")
# b2 = B("B2")

# a1.add_b(b1)
# a1.add_b(b2)
# a2.add_b(b1)

# b1.add_a(a1)
# b2.add_a(a1)
# b1.add_a(a2)

# jdb.update(asdict(a1))

# print(
#     a1.bs
# )  # Output: {'B1': B(name='B1', as_={'A1': A(name='A1', bs={'B1': B(name='B1', as_={'A1': A(name='A1', bs={}), 'A2': A(name='A2', bs={})})}), 'A2': A(name='A2', bs={})}), 'B2': B(name='B2', as_={'A1': A(name='A1', bs={'B1': B(name='B1', as_={'A1': A(name='A1', bs={}), 'A2': A(name='A2', bs={})})}), 'A2': A(name='A2', bs={})})})}
# print(
#     b1.as_
# )  # Output: {'A1': A(name='A1', bs={'B1': B(name='B1', as_={'A1': A(name='A1', bs={}), 'A2': A(name='A2', bs={})})}), 'A2': A(name='A2', bs={})}
