import sys
from package.converter import RomanNumeralConverter


if __name__ == '__main__':
    args = sys.argv
    Converter = RomanNumeralConverter()
    if len(args) == 1:
        print('No integer is given as the execution parameter.')
        Converter.AddArabianNumber()

    for i in range(len(args)):
        if i == 0:
            continue

        Converter.input_number = int(args[i])
        Converter.CheckInputNumber()

    sys.exit()
