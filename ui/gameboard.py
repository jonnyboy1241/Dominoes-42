import arcade
import os
from win32api import GetSystemMetrics

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
SCREEN_TITLE = "42 Dominoes"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True, fullscreen=False)

        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)
        arcade.set_background_color((39, 119, 20))  # The color "Pool Felt Green"
        self.example_image = arcade.load_texture(":resources:images/tiles/boxCrate_double.png")

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Get viewport dimensions
        left, screen_width, bottom, screen_height = self.get_viewport()

        # Draw some boxes on the bottom so we can see how they change
        for x in range(64, 800, 128):
            y = 64
            width = 128
            height = 128
            arcade.draw_texture_rectangle(x, y, width, height, self.example_image)


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
