"Artwork from https://kenney.nl"

import random
import arcade


# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_CREW = .25
SPRITE_SCALING_REEF = 0.5
CREW_COUNT = 50
REEF_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Save your crew"

# Speed limit
MAX_SPEED = 8.0

# How fast we accelerate
ACCELERATION_RATE = 3.0

# How fast to slow down after we let off the key
FRICTION = 0.02

class Crew(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                      SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

class Reef(arcade.Sprite):
    def reset_pos(self):

        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()

class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check to see if we hit the screen edge
        if self.left < 0:
            self.left = 0
            self.change_x = 0  # Zero x speed
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
            self.change_x = 0

        if self.bottom < 0:
            self.bottom = 0
            self.change_y = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 2
            self.change_y = 0

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.crew_list = None
        self.reef_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Track the keys pressed
        self.A_pressed = False
        self.D_pressed = False
        self.W_pressed = False
        self.S_pressed = False

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.crew_list = arcade.SpriteList()
        self.reef_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Pirate ship image from kenney.nl
        img = ":resources:images/kenney_pirate-pack/PNG/Retina/Ships/ship (2).png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the stranded crew-mates.
        for i in range(CREW_COUNT):

            # Create the Person instance
            # Crew-mate image from kenney.nl
            crew = Crew(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", SPRITE_SCALING_CREW)

            # Position the crew
            crew.center_x = random.randrange(SCREEN_WIDTH)
            crew.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the crew to the lists
            self.crew_list.append(crew)

        for i in range(REEF_COUNT):

            # Create obstacles
            reef = Reef("stoneCaveSpikeBottom.png", SPRITE_SCALING_REEF)

            # Position the obstacles
            reef.center_x = random.randrange(SCREEN_WIDTH)
            reef.center_y = random.randrange(SCREEN_HEIGHT)

            # Add reef to the lists
            self.reef_list.append(reef)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.crew_list.draw()
        self.reef_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

    def update(self, delta_time):
        self.player_sprite.update()
        self.crew_list.update()
        self.reef_list.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
    def on_update(self, delta_time):
        """ Movement and game logic """
        # Generate a list of all sprites that collided with the player.
        crews_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.crew_list)
        reef_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.reef_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for crew in crews_hit_list:
            crew.remove_from_sprite_lists()
            self.score += 1

        for reef in reef_hit_list:
            reef.remove_from_sprite_lists()
            self.score += -1

def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()