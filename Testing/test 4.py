# Artwork from https://kenney.nl
# Sounds from OpenGameArt.Org
import arcade
import random
import math

SPRITE_SCALING = .8
SPRITE_SCALING_AMMO = .5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ship Defense"

MOVEMENT_SPEED = 7
BULLET_SPEED = 5
ENEMY_BULLET_SPEED = 2

ENEMY_COUNT = 9
MAX_PLAYER_AMMO = 100
SPRITE_LIFE = 11

class Enemy(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                      SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def __init__(self, image_file, scale, enemy_bullet_list, time_between_fire):

        super().__init__(image_file, scale)



class Player(arcade.Sprite):

    def update(self):

        # Move player sprite.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds and stop sprite form moving beyond the screen.
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
# Game states
GAME_OVER = 1
PLAY_GAME = 0

class MyGame(arcade.Window):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.enemy_list = arcade.SpriteList()

        self.time_since_firing = 0.0

        self.frame_count = 0

        # Set list to the starting state.
        self.player_list = None
        self.enemy_list = None
        self.player_bullet_list =None
        self.enemy_bullet_list = None

        self.game_state = PLAY_GAME

        # Set up the player info
        self.player_sprite = None
        self.enemy_sprite = None
        self.neutralized = None

        self.physics_engine = None
        self.background = None

        # Track directional keys
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Load sounds for later use.
        self.gun_fire = arcade.load_sound("pistol3.ogg")
        self.pain = arcade.load_sound("aw01.ogg")
        self.minigun_fire = arcade.load_sound("minigun.ogg")

    def setup(self):

        # Setting all lists to a list
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()

        # Score
        self.neutralized = 0

        # Set up player sprite.
        self.player_sprite = Player("spaceAstronauts_006.png", scale=1)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Place enemies. I also tried to slow down their fire.
        for i in range(ENEMY_COUNT):
            enemy = Enemy("spaceAstronauts_018.png",
                      SPRITE_SCALING,
                          enemy_bullet_list=self.enemy_bullet_list,
                          time_between_fire=5.0)

            enemy.center_x = random.randrange(300, 800)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)
            enemy.angle = 180

            self.enemy_list.append(enemy)

        # Using texture for background
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()

        # Drawing Texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw all the sprites.
        self.player_list.draw()
        self.enemy_list.draw()
        self.player_bullet_list.draw()
        self.enemy_bullet_list.draw()

        # Insert GUI
        arcade.draw_text(f"Neutralized: {self.neutralized}", 10, 20, arcade.color.AO)

        # Game state. You failed
        if self.game_state == GAME_OVER:
            arcade.draw_text("YOU FAILED", 150, 300, arcade.color.BLACK_OLIVE, 70)
            self.set_mouse_visible(True)

    # Using the mouse to fire bullets at the enemies.
    def on_mouse_press(self, x, y, button, modifiers):

        if len(self.player_bullet_list) < MAX_PLAYER_AMMO:
            arcade.play_sound(self.gun_fire)

            bullet = arcade.Sprite("spaceMissiles_025.png", SPRITE_SCALING_AMMO)
            bullet.angle = -90

            bullet.change_x = BULLET_SPEED

            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.bottom

            self.player_bullet_list.append(bullet)

    # Player sprite movement
    def update_player_speed(self):

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    # Using delta time to edit enemy fire. No luck yet.
    def on_update(self, delta_time: float = 1 / 60):
        """ Movement and game logic """

        if self.game_state == GAME_OVER:
            return

        if len(self.enemy_list) == 0:
            return

        # Updating sprites to their proper states.
        self.player_list.update()
        self.enemy_list.update()
        self.player_bullet_list.update()
        self.enemy_bullet_list.update()
        self.enemy_list.on_update(delta_time)

        # Make enemies track and shoot at player sprite.
        for enemy in self.enemy_list:
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Setting the destination to the center of the player sprite.
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            enemy.angle - math.degrees(angle) - 90

        if self.frame_count % 60 == 0:

            # Forming enemy bullets and defining their direction.
            bullet = arcade.Sprite("spaceMissiles_024.png", SPRITE_SCALING_AMMO)
            bullet.center_x = start_x
            bullet.center_y = start_y

            bullet.angle = 90

            bullet.change_x = math.cos(angle) * ENEMY_BULLET_SPEED
            bullet.change_y = math.sin(angle) * ENEMY_BULLET_SPEED

            self.enemy_bullet_list.append(bullet)

            # If bullets pass the left border of the screen they are removed from the sprite list.
            for bullet in self.enemy_bullet_list:
                if bullet.left < 0:
                    bullet.remove_from_sprite_lists()
            self.enemy_bullet_list.update()

            # Check if bullet connects with player sprite and if it does end the game state.
            for bullet in self.enemy_bullet_list:
                if arcade.check_for_collision_with_list(self.player_sprite, self.enemy_bullet_list):
                    self.game_state = GAME_OVER

                if bullet.top < 0:
                    bullet.remove_from_sprite_lists

        self.player_bullet_list.update()

        # Checking if player bullets hit enemies and removing the hit enemies from the sprite lists.
        for bullet in self.player_bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.neutralized += 1

                # Playing the sound that I feel as I try to fix the minigun effect.
                arcade.play_sound(self.pain)

    # Tracking key presses.
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()