import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_ground():
    """ Draw the ground"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_OLIVE_GREEN)


def draw_rocket(x, y):
    """ Draw a rocket"""

    # Draw a point ar x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Draw the body of the rocket
    arcade.draw_rectangle_filled(400 + x, 350 + y, 100, 500, arcade.color.BATTLESHIP_GREY)
    arcade.draw_triangle_filled(150 + x, 100 + y, 350 + x, 100 + y, 350 + x, 300 + y, arcade.color.BONE)
    arcade.draw_triangle_filled(450 + x, 100 + y, 650 + x, 100 + y, 450 + x, 300 + y, arcade.color.BONE)
    arcade.draw_rectangle_filled(400 + x, 195 + y, 5, 190, arcade.color.BONE)

    # Draw window in rocket
    arcade.draw_rectangle_filled(400 + x, 500 + y, 60, 100, arcade.color.BONE)
    arcade.draw_rectangle_filled(400 + x, 500 + y, 40, 80, arcade.color.BLACK)

def on_draw(delta_time):
    """Draw everything"""
    arcade.start_render()

    draw_ground()
    draw_rocket(300, 50)
    draw_rocket(-200, on_draw.rocket1_y)

    # Add to the y value, making rocket move up
    on_draw.rocket1_y += 10


# Starting point for rocket
on_draw.rocket1_y = 50

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SAE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call rhe main function to get the program started.
main()