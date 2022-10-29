from enum import Enum


class Action(int, Enum):
    MoveForward = 0
    TurnRight = 1
    TurnLeft = 2
    Shoot = 3
    Grab = 4
    Release = 5
