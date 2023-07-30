from dataclasses import dataclass, asdict
import unittest
import jsoneng


@dataclass
class Char:
    name: str
    role: str
    desc: str


class Test(unittest.TestCase):
    def setUp(self):
        self.jdb = jsoneng.JsonDB()
        self.jdb.create({})

    def tearDown(self):
        self.jdb.delete()

    def test_something(self):
        name = "John"
        role = "Ruler"
        desc = "a fashionable young nobleman"

        self.char = Char(name, role, desc)

        self.jdb.patch(asdict(self.char))

        # constructor tests
        self.assertEqual(self.char.name, name)
        self.assertEqual(self.char.role, role)
        self.assertEqual(self.char.desc, desc)

        # jsoneng tests
        self.assertEqual(self.char.name, self.jdb.r("name"))
        self.assertEqual(self.char.role, self.jdb.r("role"))
        self.assertEqual(self.char.desc, self.jdb.r("desc"))
