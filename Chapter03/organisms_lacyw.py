"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 03.4- Organisms
Date: 02/21/2022

Description:
    This program predicts exponential growth in organisms based on user inputs of initial population, growth rate, and number of days

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
	
	#Prompt user for input values
	start = float(input("Starting population, in thousands: "));
	rate = float(input("Average daily increase, in percent: "));
	days = int(input("Number of days to multiply: "));
	
	#initialize population
	pop = start;
	
	#Header
	print("Day   Approx. Pop");
	#Loop through days
	for i in range(days + 1):
		print("{:>3.0f}  {:>12,.3f}".format(i, pop))
		pop *= 1 + rate / 100;

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
