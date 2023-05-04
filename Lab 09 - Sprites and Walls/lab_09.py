# Artwork from https://kenney.nl

import random
import arcade
import os
from pyglet.math import Vec2

SPRITE_SCALING = 0.4
SPRITE_SCALING_ROCKET = 0.2
SPRITE_ROOM_SIZE = 128
SPRITE_SIZE = int(SPRITE_ROOM_SIZE * SPRITE_SCALING)

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7

ROCKET_NUM = 1

class Room:

    def __init__(self):
        self.block_list = None
        self.rockets_list = None
        self.background = None
        self.block_list = None


def setup_room_1():
    room = Room()

    room.block_list = arcade.SpriteList()
    room.rockets_list = arcade.SpriteList()

    for y in (0, DEFAULT_SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, DEFAULT_SCREEN_WIDTH, SPRITE_SIZE):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.left = x
            block.bottom = y
            room.block_list.append(block)

    block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
    block.left = 7 * SPRITE_SIZE
    block.bottom = 5 * SPRITE_SIZE
    room.block_list.append(block)

    rockets = arcade.Sprite("spaceRocketParts_001.png")
    rockets.left = 2 * SPRITE_SIZE
    rockets.bottom = 1 * SPRITE_SIZE
    room.rockets_list.append(rockets)
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    return room

def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.block_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, DEFAULT_SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, DEFAULT_SCREEN_WIDTH, SPRITE_SIZE):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.left = x
            block.bottom = y
            room.block_list.append(block)

    block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
    block.left = 7 * SPRITE_SIZE
    block.bottom = 5 * SPRITE_SIZE
    room.block_list.append(block)
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    return room

def setup_room_3():
    room = Room()

    room.block_list = arcade.SpriteList()
    for y in (0, DEFAULT_SCREEN_HEIGHT - SPRITE_SIZE):
        for x in range(0, DEFAULT_SCREEN_WIDTH, SPRITE_SIZE):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.left = 7 * SPRITE_SIZE
            block.bottom = 5 * SPRITE_SIZE
            room.block_list.append(block)
            room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

            return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.rockets_list = None
        self.block_list = None
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("spaceAstronauts_001.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.rooms[self.current_room].block_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].block_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > DEFAULT_SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].block_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].block_list)
            self.player_sprite.center_x = DEFAULT_SCREEN_WIDTH


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()