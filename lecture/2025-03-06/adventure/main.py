from operator import invert

from rooms import room1, room2, room3, room4

room_list = [room1, room2, room3, room4]
inventory = []
current_room = 1
adventure_completed = False

while not adventure_completed:
    aktueller_raum = room_list[current_room]
    print(aktueller_raum.name)
    print(aktueller_raum.description)

    aktion = input("Was möchten Sie tun? ")
    if aktion == 'links' and current_room > 0:
        current_room = current_room - 1
    elif aktion == 'rechts' and current_room < 4:
        current_room = current_room + 1
    elif aktion == 'nimm':
        item = input("Was möchten Sie nehmen?")
        if item in aktueller_raum.items:
            inventory.append(item)
            aktueller_raum.items.remove(item)
        else:
            print("Dieses Item gibt es hier nicht.")


if __name__ == "__main__":
    main()