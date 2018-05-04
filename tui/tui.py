import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from tui.scenes.main_scene import MainScene


class TUI(object):
    def __init__(self):
        self.last_scene = None

    def _tui_main(self, screen):
        scenes = [
            Scene([MainScene(screen)], -1, name="Main")
        ]

        screen.play(scenes, stop_on_resize=True, start_scene=self.last_scene)

    def start(self):
        while True:
            try:
                Screen.wrapper(self._tui_main, catch_interrupt=True)
                sys.exit(0)
            except ResizeScreenError as e:
                self.last_scene = e.scene
