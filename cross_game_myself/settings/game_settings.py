from pathlib import Path

from cross_game import assets

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
COLORS = ("red", "orange", "yellow", "green", "blue", "purple")
STARTING_MOVE_DISTANCE = 2
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 275
FONT = ("Courier", 20, "bold")
PATH_TO_ASSETS = str(Path(assets.__file__).parent.absolute())
