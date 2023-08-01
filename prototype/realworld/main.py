import random
from dataclasses import dataclass, asdict
from termcolor import cprint
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


@dataclass
class Event:
    key: str
    desc: str


@dataclass
class EventMap:
    eventMap: dict


@dataclass
class Place:
    key: str
    name: str
    neighbors: list


@dataclass
class PlaceMap:
    placeMap: dict


h_livingroom = Place("h_livingroom", "Living Room", ["h_hallway"])
h_hallway = Place("h_hallway", "Hallway", ["h_livingroom", "h_door"])
h_door = Place("h_door", "House Front Door", ["h_hallway", "street"])

sm_entrance = Place(
    "sm_entrance", "Supermarket Entrance", ["street", "sm_checkout", "sm_aisle"]
)
sm_checkout = Place("sm_checkout", "Supermarket Checkout", ["sm_entrance", "sm_aisle"])
sm_aisle = Place(
    "sm_aisle",
    "Supermarket Aisle",
    [
        "sm_entrance",
        "sm_checkout",
        "sm_bakery",
        "sm_butchers",
        "sm_vegetables",
    ],
)
sm_bakery = Place("sm_bakery", "Bakery", ["sm_aisle"])
sm_butchers = Place("sm_butchers", "Butchers", ["sm_aisle"])
sm_vegetables = Place("sm_vegetables", "Vegetables", ["sm_aisle"])

street = Place("street", "A Quiet Street", ["h_door", "sm_entrance"])

h_dinner = Event(
    "h_dinner",
    "You are hungry. What do you do?",
)

h_momcallsfordinner = Event(
    "h_momcallsfordinner",
    "Your mom calls for dinner, what do you do?",
)

h_momcallsforlunch = Event(
    "h_momcallsforlunch",
    "Your mom calls for lunch, what do you do?",
)

h_pee = Event(
    "h_pee",
    "What do you do when you pee?",
)

h_boredom = Event(
    "h_boredom",
    "What do you do when you are bored?",
)

sm_deal = Event(
    "sm_deal",
    "You spot some good deals at the supermarket?",
)

sm_pee = Event(
    "sm_pee",
    "What do you do when you need to pee at the supermarket?",
)


h_events = [h_dinner, h_momcallsfordinner, h_momcallsforlunch, h_pee, h_boredom]

sm_events = [sm_deal, sm_pee]

street_events = []

w_map = PlaceMap(
    {
        "h_livingroom": h_livingroom,
        "h_hallway": h_hallway,
        "h_door": h_door,
        "sm_entrance": sm_entrance,
        "sm_checkout": sm_checkout,
        "sm_aisle": sm_aisle,
        "sm_bakery": sm_bakery,
        "sm_butchers": sm_butchers,
        "sm_vegetables": sm_vegetables,
        "street": street,
    },
)

h_livingroom.event = h_events
h_hallway.event = h_events
h_door.event = h_events
sm_entrance.event = sm_events
sm_checkout.event = sm_events
sm_aisle.event = sm_events
sm_bakery.event = sm_events
sm_butchers.event = sm_events
sm_vegetables.event = sm_events
street.event = street_events


def traverse(place_map, place_key):
    """
    Traverses through the place map starting from the given place key.
    """

    time = 0
    while True:
        time += 1
        if place_key not in place_map.placeMap:
            print(f"Invalid place key: {place_key}\n")
            place_key = input("Enter a valid place key: ")
        else:
            current_place = place_map.placeMap[place_key]
            cprint(f"You are in {current_place.name}.", "red")
            cprint(f"The time is {time}.", "blue")

            events = current_place.event or []

            if events:
                event = random.choice(events)
                cprint(f"Event: {event.desc}.\n", "yellow")

                text = input("> ")
                jdb.patch({time: {"prompt": event.desc, "answer": text}})
            else:
                cprint(f"There are no events in {current_place.name}.\n", "yellow")

            if current_place.neighbors:
                print("Places You Can Visit: ")
                for i, neighbor_key in enumerate(current_place.neighbors):
                    neighbor = place_map.placeMap[neighbor_key]
                    cprint(f"{i+1}. {neighbor.name}", "red")

                choice = input("Enter the number of the neighbor you want to go to: ")
                if choice.isdigit() and 1 <= int(choice) <= len(
                    current_place.neighbors
                ):
                    chosen_neighbor = current_place.neighbors[int(choice) - 1]
                    print(f"Moving to {place_map.placeMap[chosen_neighbor].name}...\n")
                    place_key = chosen_neighbor
                else:
                    print("Invalid neighbor choice.\n")

    # if current_place.occupants:
    #     print("Occupants: ")
    #     for occupant in current_place.occupants:
    #         print(f"- {occupant}")

    print()


def main():
    print("begins program")

    # jdb.update(asdict(w_map))
    # traverse(w_map, "h_livingroom")


if __name__ == "__main__":
    main()
