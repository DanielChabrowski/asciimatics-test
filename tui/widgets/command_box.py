from asciimatics.widgets import ListBox


class CommandBox(ListBox):

    def __init__(self, height, options, **kwargs):
        super(CommandBox, self).__init__(height=height, options=self._create_options(options),
                                         on_select=self._on_select, **kwargs)
        self.opt_functions = options

    def _on_select(self):
        self.opt_functions[self.value][1]()

    @staticmethod
    def _create_options(options):
        opt_index = 0
        numbered_options = []

        for opt in options:
            numbered_options.append((opt[0], opt_index))
            opt_index += 1

        return numbered_options
