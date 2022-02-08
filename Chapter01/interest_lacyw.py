"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 01.2 - interest
Date: 02/07/2022

Description:
    Calculates the account balance of a bank account at a specific time for a given interest rate and compounding period. Prompts user for floating point input

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
	#Prompt user with data format
	print("Enter the following parameters.");
	
	#Inputs - prompt user for specific, floating point inputs
	P = float(input("  The initial deposit? "));
	r = float(input("  The annual interest rate in percent? "));
	t = float(input("  The number of years the account earn interest? "));
	n = float(input("  The number of times interest is compounded each year: "));
	
	#Calculations - calculate the account balance
	r = r / 100;
	balance = P * pow((1 + r/n), (n * t));
	
	#Output - output the results
	print("The balance of this account will be ${:,.2f} after {:.1f} years.".format(balance, t));


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
