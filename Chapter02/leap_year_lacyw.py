"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 02.1 - Leap Year
Date: 02/14/2022

Description:
    This program calculates wether or not the inputted year is a leap year and tells the user how many days are in the February of the year they inputted

Contributors:
    William Rhodes Lacy, lacyw@purdue.edu

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    #Inputs - prompt user for integer year
	year = int(input("Enter a year: "));
	
	#Define a boolean about whether or not this is a leap year
	isLeap = ((year % 4 == 0) and (not (year % 100 == 0))) or (year % 400 == 0);
	
	#Debugging code
	"""
	print(year % 4);
	print(not year % 100);
	print(year % 400);
	print(isLeap);
	"""
	#If the given year is a leap year, tell the user it is a leap year and feb = 29 days
	if isLeap:
		print("The year {} is a leap year.".format(year));
		print("February of {} has 29 days.".format(year));
	else:
		#If the year is not a leap year, tell the user it is not a leap year and feb = 28 days
		print("The year {} is not a leap year.".format(year));
		print("February of {} has 28 days.".format(year));

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
