from specklepy.objects import Base
from specklepy.objects.geometry import Point

class Block(Base):
    length: float
    width: float
    height: float
    origin: Point = None

    def __init__(self, length=1.0, width=1.0, height=1.0, origin=Point(), **kwargs) -> None:
        super().__init__(**kwargs)
        # mark the origin as a detachable attribute
        self.add_detachable_attrs({"origin"})

        self.length = length
        self.width = width
        self.height = height
        self.origin = origin