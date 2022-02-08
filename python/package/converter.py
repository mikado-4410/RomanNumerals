import sys


class RomanNumeralConverter:
    MIN_ROMAN_NUMERAL = int(1)
    MAX_ROMAN_NUMERAL = int(3999)

    input_number = 0

    def CheckInputNumber(self):
        if (self.MIN_ROMAN_NUMERAL > self.input_number or self.input_number > self.MAX_ROMAN_NUMERAL):
            print('{} is not proper input.'.format(self.input_number))
            self.AddArabianNumber()

        self.ApplyRomanConverter()

    def AddArabianNumber(self):
        print(
            'Please enter the integer again in the range of 1 to 3999 (Enter 0 to exit).')
        self.input_number = input('Please enter a value -> ')
        if self.input_number:
            self.CheckInputNumber()
        else:
            sys.exit()

    def ApplyRomanConverter(self):
        self.i = 0
        self.romanNumber = ''
        self.correspondingValue = (
            (100, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        )
        while self.input_number:
            while (self.input_number / self.correspondingValue[self.i][0]):
                self.romanNumber += self.correspondingValue[self.i][1]
                self.input_number -= self.correspondingValue[self.i][0]

            self.i += 1

        print(self.romanNumber)
