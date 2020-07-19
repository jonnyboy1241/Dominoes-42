import arcade
from win32api import GetSystemMetrics
from game import *

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
SCREEN_TITLE = "42 Dominoes"


class GameWindow(arcade.Window):

    def __init__(self, game):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True, fullscreen=False)

        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)
        arcade.set_background_color((39, 119, 20))  # The color "Pool Felt Green"
        self.game = game

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Get viewport dimensions
        left, screen_width, bottom, screen_height = self.get_viewport()

        # Draw some boxes on the bottom so we can see how they change
        y = 60
        for player in self.game.players:
            x = 115
            for domino in player.hand.dominoes:
                image = arcade.load_texture(domino.image_path)
                arcade.draw_texture_rectangle(x, y, 210, 100, image)
                x += 215

            y += 150


def main():
    GameWindow(Game())
    arcade.run()


if __name__ == "__main__":
    main()
