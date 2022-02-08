import sys


class RomanNumeralConverter:
    MIN_ROMAN_NUMERAL = 1
    MAX_ROMAN_NUMERAL = 3999

    input_number = 0

    def CheckInputNumber(self):
        if (self.MIN_ROMAN_NUMERAL > self.input_number or self.input_number > self.MAX_ROMAN_NUMERAL):
            print('{} is not proper input.'.format(self.input_number))
            self.AddArabianNumber()

    def AddArabianNumber(self):
        print(
            'Please enter the integer again in the range of 1 to 3999 (Enter 0 to exit).\n')
        self.input_number = input('Please enter a value -> ')
        if self.input_number:
            self.CheckInputNumber()
        else:
            sys.exit()
    
    def ApplyRomanConverter(self):
        i = 0
