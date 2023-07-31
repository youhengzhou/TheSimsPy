from dataclasses import dataclass, asdict
from termcolor import cprint
import jsoneng


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

sm_entrance = Place("sm_entrance", "Supermarket Entrance", ["sm_checkout", "sm_aisle"])
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


def traverse(place_map, place_key):
    """
    Traverses through the place map starting from the given place key.
    """

    if place_key not in place_map.placeMap:
        print(f"Invalid place key: {place_key}")
        return

    current_place = place_map.placeMap[place_key]
    cprint(f"You are in {current_place.name}.", "red")

    if current_place.neighbors:
        print("Places You Can Visit: ")
        for i, neighbor_key in enumerate(current_place.neighbors):
            neighbor = place_map.placeMap[neighbor_key]
            cprint(f"{i+1}. {neighbor.name}", "red")

        choice = int(input("Enter the number of the neighbor you want to go to: "))
        if choice >= 1 and choice <= len(current_place.neighbors):
            chosen_neighbor = current_place.neighbors[choice - 1]
            print(f"Moving to {place_map.placeMap[chosen_neighbor].name}...\n")
            traverse(place_map, chosen_neighbor)
        else:
            print("Invalid neighbor choice.\n")

    # if current_place.occupants:
    #     print("Occupants: ")
    #     for occupant in current_place.occupants:
    #         print(f"- {occupant}")

    print()


def main():
    print("begins program")

    # Example usage: Traverse through the w_map starting from the "street_map"

    jdb = jsoneng.JsonDB()
    jdb.create({})

    jdb.update(asdict(w_map))
    traverse(w_map, "h_livingroom")


if __name__ == "__main__":
    main()
