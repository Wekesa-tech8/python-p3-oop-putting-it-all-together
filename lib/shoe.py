# lib/shoe.py

class Shoe:
    def __init__(self, brand, size, color="Unknown"):
        self.brand = brand
        self.color = color
        self.size = size
        self.condition = "Old"  # Initialize condition, if necessary

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        self._size = value

    def cobble(self):
        self.condition = "New"  # Set condition to "New"
        print("Your shoe is as good as new!")

# Add any additional methods you need here
