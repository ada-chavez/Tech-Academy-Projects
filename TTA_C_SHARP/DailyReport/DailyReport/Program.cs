using System;

namespace DailyReport
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("The Tech Academy \nStudent Daily Report");

            Console.WriteLine("\nWhat is your name?");
            string studentName = Console.ReadLine();

            Console.WriteLine("\nWhat course are you on?");
            string courseName = Console.ReadLine();

            Console.WriteLine("\nWhat page number?");
            string pageNum = Console.ReadLine();
            ushort pageNumber = Convert.ToUInt16(pageNum);

            Console.WriteLine("\nDo you need help with anything? Plase answer \"true\" or \"false\"?");
            string wantHelp = Console.ReadLine();
            bool needHelp = Convert.ToBoolean(wantHelp);

            Console.WriteLine("\nWere there any positive experiences you'd like to share? Please give specifics.");
            string posExperience = Console.ReadLine();

            Console.WriteLine("\nIs there any other feedack you'd like to provide? Please be specific.");
            string feedback = Console.ReadLine();

            Console.WriteLine("\nHow many hours did you study today?");
            string hours = Console.ReadLine();
            byte hoursStudied = Convert.ToByte(hours);

            Console.WriteLine("\nThank you for your answers. An Instructor will respond to this shortly. Have a great day!");
            Console.ReadLine();
        }
    }
}
