using System;

namespace MathConsoleApp
{
    class Program
    {
        static void Main()
        {
            // Takes an input from the user and multiply it by 50
            Console.WriteLine("Enter a number to be multiplied by 50:");
            int num1 = Convert.ToInt32(Console.ReadLine());
            int product = 50 * num1;
            Console.WriteLine(num1 + " X 50 = "+ product);
            Console.ReadLine();

            // Takes an input from the user and adds 25 to it
            Console.WriteLine("Enter a number to be added to 25:");
            int num2 = Convert.ToInt32(Console.ReadLine());
            int sum = 25 + num2;
            Console.WriteLine(num2 + " + 25 = " + sum);
            Console.ReadLine();

            // Takes an input from the user and divides it by 12.5
            Console.WriteLine("\nEnter a number to be divided by 12.5:");
            double num3 = Convert.ToDouble(Console.ReadLine());
            double quotient = num3 / 12.5;
            Console.WriteLine(num3 + " / 12.5 = " + quotient);
            Console.ReadLine();

            // Takes an input from the user and check if it is greater than 50 printing true or false
            Console.WriteLine("Enter a number to check if it is greater than 50:");
            int num4 = Convert.ToInt32(Console.ReadLine());
            bool greaterThan = num4 > 50;
            Console.WriteLine(num4 + " is greater than 50: " + greaterThan);
            Console.ReadLine();


            // Takes an input from the user and divides it by 7 and prints the remainder
            Console.WriteLine("Enter a number to get the remainder when divided by 7:");
            int num5 = Convert.ToInt32(Console.ReadLine());
            int mod = num5 % 7;
            Console.WriteLine("The remainder of " + num5 + " / 7 is " + mod);
            Console.ReadLine();

        }
    }
}
