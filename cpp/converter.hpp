#ifndef HELLO_H
#define HELLO_H

#include <string>

class RomanNumeralConverter
{
private:
    const static int MIN_ROMAN_NUMERAL = 1;
    const static int MAX_ROMAN_NUMERAL = 3999;

public:
    int m_inputNumber = 0;
    void CheckInputNumber();
    void AddArabinNumber();
    void ApplyRomanConverter();
};

#endif