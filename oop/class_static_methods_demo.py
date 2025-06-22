#new

class Calculator:
    """A simple calculator demonstrating @staticmethod and @classmethod usage."""

    # Class attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of *a* and *b*.

        Because this operation does not depend on the state of the class or
        any instance, it is defined as a static method.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Return the product of *a* and *b* after announcing the calculation type.

        The method receives the *cls* parameter, allowing access to class
        attributes. If subclasses override *calculation_type*, the message
        will automatically reflect the subclass value.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
