import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900


def draw_rocket(x, y):
    """ Draw a rocket"""

    # Draw the body of the rocket
    arcade.draw_rectangle_filled(400 + x, 350 + y, 100, 500, arcade.color.BATTLESHIP_GREY)
    arcade.draw_triangle_filled(150 + x, 100 + y, 350 + x, 100 + y, 350 + x, 300 + y, arcade.color.BONE)
    arcade.draw_triangle_filled(450 + x, 100 + y, 650 + x, 100 + y, 450 + x, 300 + y, arcade.color.BONE)
    arcade.draw_rectangle_filled(400 + x, 195 + y, 5, 190, arcade.color.BONE)

    # Draw window in rocket
    arcade.draw_rectangle_filled(400 + x, 500 + y, 60, 100, arcade.color.BONE)
    arcade.draw_rectangle_filled(400 + x, 500 + y, 40, 80, arcade.color.BLACK)
class Rocket:
    def __init__(self, position_x, position_y, width, height, color):

        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color
    def draw(self):
        draw_rocket(self.position_x,
                    self.position_y,)
class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create rocket
        self.rocket = Rocket(50, 50, 15, 15, arcade.color.WHITE)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.rocket.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.rocket.position_x = x
        self.rocket.position_y = y

def main():
    window = MyGame(1000, 900, "Moving")
    arcade.run()


main()