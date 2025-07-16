class RomanCalculatorError(Exception):
    pass


class InvalidRomanNumeralError(RomanCalculatorError):
    pass


class NumberOutOfRangeError(RomanCalculatorError):
    pass
