########################################################
# Drawing library
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from math import cos, sin, radians, sqrt
from svgwrite import Drawing  # type: ignore # noqa: E401
from svgwrite.shapes import Rect, Circle, Polygon  # type: ignore # noqa: E401


class Canvas:
    def __init__(self) -> None:
        """Initializes the canvas."""
        self._drawing = Drawing()

    def save(self) -> None:
        """Saves the drawing to a file."""
        self._drawing.save()

    def setname(self, name: str) -> None:
        """
        Sets the filename for the drawing.

        Args:
            name (str): Filename
        """
        self._drawing.filename = name

    def addRect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        fill: str = "white",
        stroke: str = "black",
    ) -> None:
        """
        Adds a rectangle to the canvas.

        Args:
            x (float): Top left corner X
            y (float): Top left corner Y
            w (float): Width
            h (float): Height
            fill (str, optional): Fill color. Defaults to "white".
            stroke (str, optional): Stroke color. Defaults to "black".
        """
        self._drawing.add(
            Rect(insert=(x, y), size=(w, h), fill=fill, stroke=stroke)
        )

    def addCircle(
        self,
        x: float,
        y: float,
        size: float,
        fill: str = "white",
        stroke: str = "black",
    ):
        """
        Adds a circle to the canvas.

        Args:
            x (float): Center X
            y (float): Center Y
            size (float): Radius
            fill (str, optional): Fill color. Defaults to "white".
            stroke (str, optional): Stroke color. Defaults to "black".
        """
        self._drawing.add(
            Circle(center=(x, y), r=size, fill=fill, stroke=stroke)
        )

    @staticmethod
    def _createPoints(
        x: float, y: float, apothem: float
    ) -> list[tuple[int, int]]:
        """
        Creates slightly cursed points for a hexagon.

        Args:
            x (float): Middle point X
            y (float): Middle point Y
            apothem (float): Apothem length

        Returns:
            list[tuple[int, int]]: List of points that is somewhat correct
        """
        length = 2 * apothem / sqrt(3)

        angles = [
            radians(60),
            radians(0),
            radians(-60),
            radians(-120),
            radians(180),
            radians(120),
        ]

        points = [
            (
                round(x + length * cos(angle)),
                round(y - length * sin(angle)),
            )
            for angle in angles
        ]
        return points

    def addHexagon(
        self,
        x: float,
        y: float,
        apothem: float,
        fill: str = "white",
        stroke: str = "black",
    ):
        """Adds a slightly cursed hexagon to the canvas.

        Args:
            x (float): Middle point X
            y (float): Middle point Y
            apothem (float): Apothem length
            fill (str, optional): Fill color. Defaults to "white".
            stroke (str, optional): Stroke color. Defaults to "black".

        """
        self._drawing.add(
            Polygon(
                points=Canvas._createPoints(x, y, apothem),
                fill=fill,
                stroke=stroke,
            )
        )


if __name__ == "__main__":

    def print_points(points):
        formatted_points = " ".join(f"{x},{y}" for x, y in points)
        print("  ", formatted_points)

    print("x75, y75, a60:")
    print_points(Canvas._createPoints(75, 75, 60))

    print("x150, y75, a40:")
    print_points(Canvas._createPoints(150, 75, 40))

    print("x225, y75, a50:")
    print_points(Canvas._createPoints(225, 75, 50))
