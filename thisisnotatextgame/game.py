
from adventurelib import Room, when, start


current_room = starting_room = Room("""
        I don't know what you think you're doing here.
        """)

library_room = starting_room.north = Room("""
        You finally found the library! This room contains an item that you
        will need to complete your mission.
        """)

storage_room = library_room.north = Room("""
        This is the storage room. If you look properly you will find a key
        """)

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        print('You go %s.' % direction)
        look()


@when('look')
def look():
    print(current_room)
    if hasattr(current_room, 'items'):
        for i in current_room.items:
            print('A %s is here.' % i)


@when('ignore narrator')
def win():
    print("you win")


look()

start(help=False)
