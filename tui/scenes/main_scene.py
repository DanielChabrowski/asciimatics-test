import logging

from asciimatics.exceptions import StopApplication
from asciimatics.widgets import Frame, Layout, Widget
from tui.widgets.command_box import CommandBox


class MainScene(Frame):
    def __init__(self, screen):
        super(MainScene, self).__init__(screen, screen.height, screen.width, title="Main scene")

        self.logger = logging.getLogger("MainScene")

        layout = Layout([10, 80], fill_frame=True)
        self.add_layout(layout)

        commands = [
            ("Clone", self.do_clone),
            ("Install", self.do_install),
            ("Quit", self.do_quit)
        ]
        self.command_box = CommandBox(Widget.FILL_FRAME, commands, name="Commands")
        layout.add_widget(self.command_box, 0)

        self.fix()

    def do_clone(self):
        self.logger.info("Selected clone command")

    def do_install(self):
        self.logger.info("Selected install command")

    def do_quit(self):
        self.logger.info("Closing application")
        raise StopApplication("User pressed quit")
