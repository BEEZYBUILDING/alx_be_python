# class_static_methods_demo.py

class Calculator:
    # Class attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Prints the calculation type using cls, then returns a * b."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
