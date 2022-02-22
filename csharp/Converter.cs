using System;
namespace csharp
{
    class RomanNumeralConverter
    {
        private const int MIN_ROMAN_NUMERAL = 1;
        private const int MAX_ROMAN_NUMERAL = 3999;

        public int m_inputNumber = 0;
        public void CheckInputNumber()
        {
            if (MIN_ROMAN_NUMERAL > m_inputNumber || m_inputNumber > MAX_ROMAN_NUMERAL)
            {
                Console.WriteLine($"{m_inputNumber} is not proper input.");
                AddArabianNumber();
            }

            ApplyRomanConverter();
        }

        public void AddArabianNumber()
        {
            Console.WriteLine($"Please enter the integer again in the range of 1 to 3999 (Enter 0 to exit).");
            Console.Write("Please enter a value -> ");
            m_inputNumber = int.Parse(Console.ReadLine());

            if (m_inputNumber == 0)
            {
                Environment.Exit(0);
            }
            else
            {
                CheckInputNumber();
            }
        }

        public void ApplyRomanConverter()
        {
            int i = 0;
            string romaNumber = "";
            Tuple<int, string>[] corresponingValue = {
                Tuple.Create(100, "M"),
                Tuple.Create(900, "CM"),
                Tuple.Create(500, "D"),
                Tuple.Create(400, "CD"),
                Tuple.Create(100, "C"),
                Tuple.Create(90, "XC"),
                Tuple.Create(50, "L"),
                Tuple.Create(40, "XL"),
                Tuple.Create(10, "X"),
                Tuple.Create(9, "IX"),
                Tuple.Create(5, "V"),
                Tuple.Create(4, "IV"),
                Tuple.Create(1, "I")
            };

            while (m_inputNumber != 0)
            {
                while (m_inputNumber / corresponingValue[i].Item1 != 0)
                {
                    romaNumber += corresponingValue[i].Item2;
                    m_inputNumber -= corresponingValue[i].Item1;
                }
                i++;
            }

            Console.Write(romaNumber);
        }
    }
}