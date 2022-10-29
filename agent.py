from enum import Enum


class Direction(Enum):
    Up = 1
    Down = 2
    Left = 3
    Right = 4


class Agent:
    # X, Y
    x = 0
    y = 0
    pit_positions = set([])
    safe_positions = []
    unsafe_positions = set([])
    breeze_positions = set([])
    seen = set([])
    walls = -1, 5
    direction = Direction.Right

    def position(self):
        return self.x, self.y

    def in_wall(self):
        min, max = self.walls

        if self.x < min or self.x > max or self.y < min or self.y > max:
            return True
        return False

    def forward(self):
        match self.direction:
            case Direction.Right:
                self.x += 1
            case Direction.Left:
                self.x -= 0
            case Direction.Up:
                self.y -= 1
            case Direction.Down:
                self.y += 1

    def turn(self, right=False):
        if right:
            if self.direction == Direction.Right:
                self.direction = Direction.Down
        else:
            if self.direction == Direction.Down:
                pass
            self.direction = Direction.Left
