
from adventurelib import Room, when, start

Room.complete = False

current_room = starting_room = Room("""
        I don't know what you think you're doing here.
        This is not even a game, don't ask for help
        """)

starting_room.complete = True

library_room = starting_room.north = Room("""
        You finally found the library! This room contains an item that you
        will need to complete your mission.
        """)

storage_room = starting_room.west = Room("""
        This is the storage room. If you look properly you will find a key
        """)

scary_room = starting_room.south = Room("""
            This is mosty scary room of all time.
""")

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room

    if current_room.complete:
        room = current_room.exit(direction)
        if room:
            current_room = room
            print('You go %s.' % direction)
            look()
    else:
        print ("You haven't completed the current one")
        pass


@when('look')
def look():
    print(current_room)
    if hasattr(current_room, 'items'):
        for i in current_room.items:
            print('A %s is here.' % i)


@when('scream')
def scream():
    if current_room is scary_room:
        scary_room.complete = True
    elif current_room is library_room:
        print("you don't have to be scared, you should be reading some book now")
    else:
        print("hahahaha why are you scared?")

@when('ignore narrator')
def win():
    print("you win")

look()

start()
