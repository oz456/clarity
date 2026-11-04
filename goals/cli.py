import argparse
import sys
from .ui.app import GoalsApp
from . import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="clarity",
        description="Clarity - A minimal, calm 2-pane goals & work manager for the terminal.",
    )
    parser.add_argument("-v", "--version", action="version", version=f"clarity {__version__}")
    parser.parse_args()

    app = GoalsApp()
    app.run()


if __name__ == "__main__":
    main()
