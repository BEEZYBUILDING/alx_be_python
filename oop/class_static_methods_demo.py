
# class_static_methods_demo.py

class Calculator:
    # Class attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Prints calculation_type via cls, then returns the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    
        

