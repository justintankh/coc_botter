from enum import Enum

class BotState(Enum):
    INITIALIZING = 0
    SEARCHING = 1
    MOVING = 2
    CLICKING = 3
    WAITING = 4
    END = 5

class Bot: