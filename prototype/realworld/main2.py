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
    items: list


@dataclass
class PlaceMap:
    placeMap: dict


@dataclass
class Item:
    name: str
    description: str


h_livingroom = Place(
    "h_livingroom",
    "Living Room",
    ["h_hallway"],
    [Item("Key", "A small key"), Item("Note", "A mysterious note")],
)
h_hallway = Place(
    "h_hallway",
    "Hallway",
    ["h_livingroom", "h_door"],
    [Item("Lamp", "A table lamp"), Item("Coat", "A coat")],
)
h_door = Place(
    "h_door",
    "House Front Door",
    ["h_hallway", "street"],
    [Item("Mail", "A letter"), Item("Shoes", "A pair of shoes")],
)
sm_entrance = Place(
    "sm_entrance",
    "Supermarket Entrance",
    ["street", "sm_checkout", "sm_aisle"],
    [Item("Cart", "A shopping cart"), Item("Flyer", "A supermarket flyer")],
)
sm_checkout = Place(
    "sm_checkout",
    "Supermarket Checkout",
    ["sm_entrance", "sm_aisle"],
    [Item("Groceries", "A bag of groceries"), Item("Receipt", "A receipt")],
)
sm_aisle = Place(
    "sm_aisle",
    "Supermarket Aisle",
    ["sm_entrance", "sm_checkout", "sm_bakery", "sm_butchers", "sm_vegetables"],
    [Item("Bread", "A loaf of bread"), Item("Meat", "A pack of meat")],
)
sm_bakery = Place(
    "sm_bakery",
    "Bakery",
    ["sm_aisle"],
    [Item("Cake", "A delicious cake"), Item("Croissant", "A freshly baked croissant")],
)
sm_butchers = Place(
    "sm_butchers",
    "Butchers",
    ["sm_aisle"],
    [Item("Steak", "A juicy steak"), Item("Sausages", "A pack of sausages")],
)
sm_vegetables = Place(
    "sm_vegetables",
    "Vegetables",
    ["sm_aisle"],
    [Item("Carrots", "A bunch of carrots"), Item("Lettuce", "A head of lettuce")],
)
street = Place(
    "street",
    "A Quiet Street",
    ["h_door", "sm_entrance"],
    [Item("Newspaper", "A newspaper"), Item("Bike", "A bicycle")],
)


h_dinner = Event("h_dinner", "You are hungry. What do you do?")
h_momcallsfordinner = Event(
    "h_momcallsfordinner", "Your mom calls for dinner, what do you do?"
)
h_momcallsforlunch = Event(
    "h_momcallsforlunch", "Your mom calls for lunch, what do you do?"
)
h_pee = Event("h_pee", "What do you do when you pee?")
h_boredom = Event("h_boredom", "What do you do when you are bored?")
sm_deal = Event("sm_deal", "You spot some good deals at the supermarket?")
sm_pee = Event("sm_pee", "What do you do when you need to pee at the supermarket?")

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

e_map = EventMap(
    {
        "h_livingroom": h_events,
        "h_hallway": h_events,
        "h_door": h_events,
        "sm_entrance": sm_events,
        "sm_checkout": sm_events,
        "sm_aisle": sm_events,
        "sm_bakery": sm_events,
        "sm_butchers": sm_events,
        "sm_vegetables": sm_events,
        "street": street_events,
    }
)


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

            events = e_map.eventMap.get(current_place.key, [])

            if events:
                event = random.choice(events)
                cprint(f"Event: {event.desc}.\n", "yellow")

                text = input("> ")
                jdb.patch({time: {"prompt": event.desc, "answer": text}})
            else:
                cprint(f"There are no events in {current_place.name}.\n", "yellow")

            if current_place.items:
                print("Items Available")
                for i, item in enumerate(current_place.items):
                    print(f"{i+1}. {item.name} - {item.description}")

                item_choice = input(
                    "Enter the number of the item you want to interact with (or '0' to skip): "
                )
                if item_choice.isdigit() and 1 <= int(item_choice) <= len(
                    current_place.items
                ):
                    chosen_item = current_place.items[int(item_choice) - 1]
                    print(
                        f"You interact with {chosen_item.name} - {chosen_item.description}\n"
                    )
                    # Implement the logic for the interaction with the chosen item
                elif item_choice == "0":
                    print("You choose not to interact with any item.\n")
                else:
                    print("Invalid item choice.\n")

            print("Neighbors:")
            for i, neighbor in enumerate(current_place.neighbors):
                print(f"{i+1}. {neighbor}")

            neighbor_choice = input(
                "Enter the number of the neighbor you want to go to: "
            )
            if neighbor_choice.isdigit() and 1 <= int(neighbor_choice) <= len(
                current_place.neighbors
            ):
                place_key = current_place.neighbors[int(neighbor_choice) - 1]
                print("\n")
            else:
                print("Invalid neighbor choice.\n")


def main():
    print("begins program")

    # Example usage: Traverse through the w_map starting from the "h_livingroom"

    jdb.update(asdict(w_map))

    traverse(w_map, "h_livingroom")


if __name__ == "__main__":
    main()
