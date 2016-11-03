
from adventurelib import Room, when, start


room_1 = Room("""
        I don't know what you think you're doing here.
        """)

current_room = room_1


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
