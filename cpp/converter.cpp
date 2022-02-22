#include <iostream>
#include <string>
#include <limits>
#include <stdlib.h>
#include <vector>
#include "converter.hpp"

void RomanNumeralConverter::CheckInputNumber()
{
    if (MIN_ROMAN_NUMERAL > this->m_inputNumber || this->m_inputNumber > MAX_ROMAN_NUMERAL)
    {
        std::cout << this->m_inputNumber << " is not proper input." << std::endl;
        this->AddArabinNumber();
    }

    this->ApplyRomanConverter();
}

void RomanNumeralConverter::AddArabinNumber()
{
    std::cout << "Please enter the integer again in the range of 1 to 3999 (Enter 0 to exit)." << std::endl;
    std::cout << "Please enter a value -> ";
    std::cin >> this->m_inputNumber;

    if (m_inputNumber)
    {
        this->CheckInputNumber();
    }
    else
    {
        std::exit(EXIT_FAILURE);
    }
}

void RomanNumeralConverter::ApplyRomanConverter()
{
    int i = 0;
    std::string romanNumber;
    std::vector<std::pair<int, std::string>> correspondingValue =
    {
        {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"},
        {50, "L"}, {40, "XL"}, {10, "X"}, {9 , "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
    };

    while (this->m_inputNumber)
    {
        while (m_inputNumber / correspondingValue[i].first)
        {
            romanNumber += correspondingValue[i].second;
            this->m_inputNumber -= correspondingValue[i].first;
        }
        i++;
    }

    std::cout << romanNumber;
}

