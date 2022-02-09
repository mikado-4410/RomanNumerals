using System;

namespace csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            RomanNumeralConverter converter = new RomanNumeralConverter();
            if (args.Length == 0)
            {
                Console.WriteLine("No integer is given as the execution parameter.");
                converter.AddArabianNumber();
            }

            for (int i = 0; i < args.Length; i++)
            {
                converter.m_inputNumber = int.Parse(args[i]);
                converter.CheckInputNumber();
            }

            return;
        }
    }
}
