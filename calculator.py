class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1,num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

# Testing code
def test_calculator():
    calculator = Calculator()

    assert calculator.add(1, 2) == 3
    assert calculator.subtract(5, 3) == 2
    assert calculator.multiply(2, 3) == 6
    assert calculator.divide(6, 2) == 3

    try:
        calculator.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"