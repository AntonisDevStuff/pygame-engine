import pyxora

class Game(pyxora.Scene):
    def _start(self):
        self.background_color = "orange"

    def _update(self):
        print(f"fps: {round(self.fps)} | dt {self.dt}")

    def _draw(self):
        pass
