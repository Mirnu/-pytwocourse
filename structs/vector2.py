class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_tuple(self) -> tuple[float, float]:
        return tuple([self.x, self.y])
    
    @staticmethod
    def zero():
        return Vector2(0, 0)
