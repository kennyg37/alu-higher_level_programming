class Base:
    """
    The `Base` class provides a base class for creating objects with unique identifiers.

    Attributes:
        id (int): A unique identifier for the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the `Base` class.

        Args:
            id (int, optional): An optional unique identifier for the object. If not provided, a new
                unique identifier is generated automatically.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
