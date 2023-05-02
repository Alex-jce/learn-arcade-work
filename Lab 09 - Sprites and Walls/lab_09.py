# Artwork from https://kenney.nl

import random
import arcade
from pyglet.math import Vec2
import math
import os

SPRITE_SCALING = 0.4
SPRITE_SCALING_ROCKET = 0.2
SPRITE_SCALING_ENEMIES = 0.5
SPRITE_SCALING_BULLET = 1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Gather Rockets and defeat enemies"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# Camera movement to keep player sprite in sight.
CAMERA_SPEED = 0.1

# Speed for sprites
PLAYER_MOVEMENT_SPEED = 7
LASER_SPEED = 6
BULLET_SPEED = 5

# Amount of sprites created.
ROCKET_COUNT = 10
ENEMY_COUNT = 50

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.block_list = None
        self.rockets_list = None
        self.laser_list = None

        # Set up the player and player interactions
        self.player_sprite = None
        self.collected = 0
        self.collected = 0
        self.enemies_killed = 0

        self.set_mouse_visible(True)

        # Prevent sprites from walking through each other
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False


        # Create the cameras. One for the GUI, one for the sprites.
        # The GUI stays on screen even as the other camera moves with the player sprite.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists also assigning the sprite lists to a list.
        self.all_sprite_list = None
        self.block_list = arcade.SpriteList()
        self.rockets_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()

        # Player Sprite
        self.player_sprite = arcade.Sprite("spaceAstronauts_001.png",
                                           scale=0.5)
        self.player_sprite.center_x = 10
        self.player_sprite.center_y = -920

        # Set up walls
        for y in range(-1000, 2000, 64):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.center_x = -150
            block.center_y = y
            self.block_list.append(block)
        for y in range(-1000, 2000, 64):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.center_x = 2000
            block.center_y = y
            self.block_list.append(block)
        for y in range(-1000, 1900, 64):
            block = arcade.Sprite("spaceBuilding_006.png",SPRITE_SCALING)
            block.center_x = 925
            block.center_y = y
            self.block_list.append(block)
        for x in range(-150, 1980, 64):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.center_x = x
            block.center_y = -1000
            self.block_list.append(block)
        for x in range(-150, 1980, 64):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.center_x = x
            block.center_y = 2000
            self.block_list.append(block)
        for x in range(-150, 870, 64):
            block = arcade.Sprite("spaceBuilding_006.png", SPRITE_SCALING)
            block.center_x = x
            block.center_y = -880
            self.block_list.append(block)

        # Use a search to stop sprites from spawning on top of each other.
        for i in range(ENEMY_COUNT):
            enemies = arcade.Sprite("spaceAstronauts_018.png", scale=1)
            enemies_placed = False
            while not enemies_placed:
                enemies.center_x = random.randrange(100, 2000, 100)
                enemies.center_y = random.randrange(100, 2000, 150)
                block_hit_list = arcade.check_for_collision_with_list(enemies, self.rockets_list,
                                                                    self.block_list)
                enemies_hit_list = arcade.check_for_collision_with_list(enemies, self.rockets_list,
                                                                       self.block_list)
                if len(block_hit_list) == 0 and len(enemies_hit_list) == 0:
                    enemies_placed = True
                    self.enemies_list.append(enemies)

        for i in range(ROCKET_COUNT):
            rockets = arcade.Sprite("spaceRocketParts_001.png", SPRITE_SCALING_ROCKET)
            rockets_placed = False
            while not rockets_placed:
                rockets.center_x = random.randrange(100, 2000, 100)
                rockets.center_y = random.randrange(100, 2000, 150)

                block_hit_list = arcade.check_for_collision_with_list(rockets, self.enemies_list,
                                                                      self.block_list)

                enemies_hit_list = arcade.check_for_collision_with_list(rockets, self.enemies_list,
                                                                        self.block_list)

                if len(block_hit_list) == 0 and len(enemies_hit_list) == 0:
                    rockets_placed = True

                    self.rockets_list.append(rockets)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.block_list)

        # Set the background color
        arcade.set_background_color(arcade.color.GREEN_YELLOW)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        #
        self.camera_sprites.use()

        # Draw the sprites.
        self.block_list.draw()
        self.player_sprite.draw()
        self.rockets_list.draw()
        self.laser_list.draw()
        self.enemies_list.draw()

        # Activate the GUI

        self.camera_gui.use()

        # Put info on the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.AO)
        text = f"collected: ({self.collected})"

        arcade.draw_text(text, 10, 10, arcade.color.BATTLESHIP_GREY, 20)
        text = f"enemies_killed: ({self.enemies_killed})"
        arcade.draw_text(text, 400, 10, arcade.color.BATTLESHIP_GREY, 20)
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

    # Aim and fire lasers with mouse.
    def on_mouse_press(self, x, y, button, modifiers):

        laser = arcade.Sprite("spaceMissiles_029.png", SPRITE_SCALING_BULLET)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        laser.center_x = start_x
        laser.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        laser.angle = math.degrees(angle)

        laser.change_x = math.cos(angle) * LASER_SPEED
        laser.change_y = math.sin(angle) * LASER_SPEED

        self.laser_list.append(laser)

    # Execute actions from code
    def on_update(self, delta_time):

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        # Assign directional keys
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Check if the rocket comes in contact with the player sprite and add points.
        rockets_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.rockets_list)
        for rockets in rockets_hit_list:
            rockets.remove_from_sprite_lists()
            self.collected += 1

        # Player weapon and collision with the enemy and walls
        for laser in self.laser_list:
            false_hit_list = arcade.check_for_collision_with_list(laser, self.block_list)
            if len(false_hit_list) > 0:
                laser.remove_from_sprite_lists()

            hit_list = arcade.check_for_collision_with_list(laser, self.enemies_list)
            if len(hit_list) > 0:
                laser.remove_from_sprite_lists()
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.enemies_killed += 1

                # Update lists
                self.physics_engine.update()
                self.rockets_list.update()
                self.block_list.update()
                self.enemies_list.update()
                self.laser_list.update()

        self.scroll_to_player()

    # Scroll screen to player sprite
    def scroll_to_player(self):

        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)



    def on_resize(self, width, height):

        self.camera_sprites.resize(int(width), int(height))

        self.camera_gui.resize(int(width), int(height))


def main():
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()