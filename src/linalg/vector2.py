

class Vector2:
    def __init__(self, x: float, y: float):
        """Create a 2D vector of the form: [x, y]

        Args:
            x : float
                The X component of the vector
            y : float
                The y component of the vector
        """
        self.x = x
        self.y = y

    def __eq__(self, other: "Vector2"):
        return (self.x == other.x) and (self.y == other.y)
    
    def zero() -> "Vector2":
        """Creates a new ZERO vector
        
        Returns:
            Vector2: A newly created 2D ZERO vector
        """
        return Vector2(0, 0)

    