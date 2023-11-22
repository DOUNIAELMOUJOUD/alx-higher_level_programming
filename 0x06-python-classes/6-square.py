Untitled document
cd alx-higher_level_programming

cd 0x06-python_classes_objects

Readme


# 0x06. Python - Classes and Objects

A project designed to give me a first hand experiece of class and objects

in python programming. Made up of 0 - 6 mandatory tasks and some advanced

tasks as follows:

### 0. My first square

An empty class Suare that defines a square

### 1. Square with size

A class Square that defines a square by: (based on 0-square.py)

### 2. Size validation

A class Square that defines a square by: (based on 1-square.py)

### 3. Area of a square

A class Square that defines a square by: (based on 2-square.py)

### 4. Access and update private attribute

A class Square that defines a square by: (based on 3-square.py)

### 5. Printing a square

A class Square that defines a square by: (based on 4-square.py)

### 6. Coordinates of a square

A class Square that defines a square by: (based on 5-square.py)




vi 0-square


#!/usr/bin/python3

"""A module for square"""



class Square:

    """Represent a square."""

    pass


vi 1-square


#!/usr/bin/python3

"""Square module."""



class Square:

    """Defines a square."""


    def __init__(self, size):

        """Constructor.

        Args:

            size: length of side of the square.

        """

        self.__size = size


vi 2-square

#!/usr/bin/python3

"""Define a class Square."""



class Square:

    """Represent a square."""


    def __init__(self, size=0):

        """Initialize a new Square.

        Args:

            size (int): The size of the new square.

        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        self.__size = size


vi 3-square

#!/usr/bin/python3

"""Define a class Square."""



class Square:

    """Represent a square."""


    def __init__(self, size=0):

        """Initialize a new square.

        Args:

            size (int): The size of the new square.

        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        self.__size = size


    def area(self):

        """Return the current area of the square."""

        return (self.__size * self.__size)


vi 4-square

#!/usr/bin/python3

"""Define a class Square."""



class Square:

    """Represent a square."""


    def __init__(self, size=0):

        """Initialize a new square.

        Args:

            size (int): The size of the new square.

        """

        self.size = size


    @property

    def size(self):

        """Get/set the current size of the square."""

        return (self.__size)


    @size.setter

    def size(self, value):

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value


    def area(self):

        """Return the current area of the square."""

        return (self.__size * self.__size)


vi 5-square

#!/usr/bin/python3

"""Define a class Square."""



class Square:

    """Represent a square."""


    def __init__(self, size):

        """Initialize a new square.

        Args:

            size (int): The size of the new square.

        """

        self.size = size


    @property

    def size(self):

        """Get/set the current size of the square."""

        return (self.__size)


    @size.setter

    def size(self, value):

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value


    def area(self):

        """Return the current area of the square."""

        return (self.__size * self.__size)


    def my_print(self):

        """Print the square with the # character."""

        for i in range(0, self.__size):

            [print("#", end="") for j in range(self.__size)]

            print("")

        if self.__size == 0:

            print("")

vi  6-square

#!/usr/bin/python3

"""Define a class Square."""



class Square:

    """Represent a square."""


    def __init__(self, size=0, position=(0, 0)):

        """Initialize a new square.

        Args:

            size (int): The size of the new square.

            position (int, int): The position of the new square.

        """

        self.size = size

        self.position = position


    @property

    def size(self):

        """Get/set the current size of the square."""

        return (self.__size)


    @size.setter

    def size(self, value):

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value


    @property

    def position(self):

        """Get/set the current position of the square."""

        return (self.__position)


    @position.setter

    def position(self, value):

        if (not isinstance(value, tuple) or

                len(value) != 2 or

                not all(isinstance(num, int) for num in value) or

                not all(num >= 0 for num in value)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value


    def area(self):

        """Return the current area of the square."""

        return (self.__size * self.__size)


    def my_print(self):

        """Print the square with the # character."""

        if self.__size == 0:

            print("")

            return


        [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):

            [print(" ", end="") for j in range(0, self.__position[0])]

            [print("#", end="") for k in range(0, self.__size)]

            print("")
