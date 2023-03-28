import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
MOVEMENT_SPEED = 5

def draw_background():
    """Draw the background"""
    # Draw Mountain
    arcade.draw_polygon_filled([[0, 350],
                                [50, 470],
                                [280, 50],
                                [0, 50]],
                               arcade.color.BLACK)
    arcade.draw_polygon_filled([[0, 350],
                                [150, 325],
                                [280, 50],
                                [0, 50]],
                               arcade.color.BLACK)
    # Draw Dark Moon
    arcade.draw_circle_filled(1000, 900, 200, arcade.color.BLACK)
    # Draw Foreground
    arcade.draw_lrtb_rectangle_filled(0, 1000, 140, 0, arcade.color.DARK_OLIVE_GREEN)

def draw_rocket(x, y):
    """ Draw a rocket"""

    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Draw the body of the rocket
    arcade.draw_rectangle_filled(+ x, + y - 155, 100, 500, arcade.color.BATTLESHIP_GREY)
    arcade.draw_triangle_filled(50 + x, y - 405, 250 + x, y - 405, 50 + x, y - 205, arcade.color.BONE)
    arcade.draw_triangle_filled(x - 50, y - 405, x - 250, y - 405, x - 50, y - 205, arcade.color.BONE)
    arcade.draw_rectangle_filled(+ x, y - 310, 5, 190, arcade.color.BONE)
    arcade.draw_triangle_filled(x - 50, y + 95, + x, y + 170, 50 + x, y + 95, arcade.color.BLACK_OLIVE)

    # Draw window in rocket
    arcade.draw_rectangle_filled(+ x, y - 10, 60, 100, arcade.color.BONE)
    arcade.draw_rectangle_filled(+ x, y - 10, 40, 80, arcade.color.BLACK)
class Rocket:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
    def draw(self):
        draw_rocket(self.position_x,
                    self.position_y,)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the rocket hits the edge of the screen. If so, change direction
        if self.position_x < self.width:
            self.position_x = self.width

        if self.position_x > SCREEN_WIDTH - self.width:
            self.position_x = SCREEN_WIDTH - self.width

        if self.position_y < self.height:
            self.position_y = self.height

        if self.position_y > SCREEN_HEIGHT - self.height:
            self.position_y = SCREEN_HEIGHT - self.height
class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SAE)

        # Create rocket
        self.rocket = Rocket(500, 450, 0, 0, 15, 15, arcade.color.WHITE)
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        draw_background()
        self.rocket.draw()

    def update(self, delta_time):
        self.rocket.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.rocket.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.rocket.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.rocket.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.rocket.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.rocket.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.rocket.change_y = 0

def main():
    window = MyGame(1000, 900, "Moving with arrows")
    arcade.run()


main()