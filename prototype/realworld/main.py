from dataclasses import dataclass


@dataclass
class Place:
    key: str
    name: str
    exit: bool
    neighbors: list


@dataclass
class PlaceMap:
    key: str
    placeMap: dict
    neighbors: list


h_livingroom = Place("h_livingroom", "Living Room", False, ["h_hallway"])
h_hallway = Place("h_hallway", "Hallway", False, ["h_livingroom", "h_door"])
h_door = Place("h_door", "Door", True, ["h_hallway"])

h_map = PlaceMap(
    "h_map",
    {
        "h_livingroom": h_livingroom,
        "h_hallway": h_hallway,
        "h_door": h_door,
    },
    ["street_map"],
)

sm_aisle = Place("sm_aisle", "Aisle", False, [])
sm_bakery = Place("sm_bakery", "Bakery", False, ["sm_aisle"])
sm_butchers = Place("sm_butchers", "Butchers", False, ["sm_aisle"])
sm_vegetables = Place("sm_vegetables", "Vegetables", False, ["sm_aisle"])

sm_map = PlaceMap(
    "sm_map",
    {
        "sm_aisle": sm_aisle,
        "sm_bakery": sm_bakery,
        "sm_butchers": sm_butchers,
        "sm_vegetables": sm_vegetables,
    },
    ["street_map"],
)

street = Place("street", "Street", False, [])

street_map = PlaceMap("street_map", {}, [h_map, sm_map])

w_map = PlaceMap(
    "w_map",
    {
        "h_map": h_map,
        "sm_map": sm_map,
        "street_map": street_map,
    },
    [],
)


def traverse(place_map, place_key):
    """
    Traverses through the place map starting from the given place key.
    """

    if place_key not in place_map:
        print(f"Invalid place key: {place_key}")
        return

    current_place = place_map.placeMap[place_key]
    print(f"You are in {current_place.name}.")

    if current_place.exit:
        print("This place has an exit.")

    if current_place.neighbors:
        print("Neighbors: ")
        for i, neighbor_key in enumerate(current_place.neighbors):
            neighbor = place_map.placeMap[neighbor_key]
            print(f"{i+1}. {neighbor.name}")

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


traverse(h_map, "h_livingroom")


if __name__ == "__main__":
    main()
