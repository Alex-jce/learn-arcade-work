# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Lab")

# Set the background color
arcade.set_background_color(arcade.color.SAE)

# Get ready to draw
arcade.start_render()

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

# Draw a rocket
arcade.draw_rectangle_filled(400, 300, 100, 600, arcade.color.BATTLESHIP_GREY)
arcade.draw_triangle_filled(150, 100, 350, 100, 350, 300, arcade.color.BONE)
arcade.draw_triangle_filled(450, 100, 650, 100, 450, 300, arcade.color.BONE)
arcade.draw_rectangle_filled(400, 180, 5, 227, arcade.color.BONE)

# Draw window in rocket
arcade.draw_rectangle_filled(400, 500, 60, 100, arcade.color.BONE)
arcade.draw_rectangle_filled(400, 500, 40, 80, arcade.color.BLACK)

# Draw Dark Moon
arcade.draw_circle_filled(775, 550, 150, arcade.color.BLACK)

# Draw Foreground
arcade.draw_lrtb_rectangle_filled(0, 800, 140, 0, arcade.color.DARK_OLIVE_GREEN)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until closed.
arcade.run()