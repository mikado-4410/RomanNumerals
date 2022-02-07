#include <iostream>
#include "converter.hpp"

int main(int argc, char *argv[])
{
    if (argc == 1)
    {
        std::cerr << "No integer is given as the execution parameter." << std::endl;
    }

    RomanNumeralConverter Converter;
    for (int i = 1; i < argc; i++)
    {
        Converter.m_inputNumber = atoi(argv[i]);
        Converter.CheckInputNumber();
    }

    printf("\n");

    return EXIT_SUCCESS;
}