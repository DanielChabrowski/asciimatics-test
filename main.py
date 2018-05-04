import logging

from tui.tui import TUI


def setup_logger():
    log_handler = logging.FileHandler('logs.txt', mode='w')
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, handlers=[log_handler], format=log_format)


def main():
    setup_logger()

    ui = TUI()
    ui.start()


if __name__ == "__main__":
    main()
