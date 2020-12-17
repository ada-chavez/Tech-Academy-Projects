using System;

namespace AnonymousIncomeComparison
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Anonymous Income Comparison Program\nPerson 1");

            // Input for Person 1
            Console.WriteLine("Hourly Rate?");
            double rateOne = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Hours worked per week?");
            double weekOne = Convert.ToDouble(Console.ReadLine());

            // Input for Person 2
            Console.WriteLine("Person 2 \nHourly Rate?");
            double rateTwo = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Hours worked per week?");
            double weekTwo = Convert.ToDouble(Console.ReadLine());
            
            // Calculates annual salary 
            double salaryOne = 52 * (rateOne * weekOne);
            double salaryTwo = 52 * (rateTwo * weekTwo);

            Console.WriteLine("Annual salary of Person 1:\n" + salaryOne);
            Console.WriteLine("Annual salary of Person 2:\n" + salaryTwo);

            // Is annual salary of Person 1 greater than Person 2?
            bool makeMore = salaryOne > salaryTwo;
            Console.WriteLine("Does Person 1 make more money than Person 2?\n" + makeMore);

            Console.ReadLine();
        }
    }
}
