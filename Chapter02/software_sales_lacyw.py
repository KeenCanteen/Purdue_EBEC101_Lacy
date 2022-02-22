"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 02.2 - Software sales
Date: 02/14/2022

Description:
    This program calculates the amount of discount a user is qualified for based on the input quantity of items purchased

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
	#Prompt the user for an integer number of packages purchased
	amt = int(input("How many packages will be purchased: "));
	
	#Define the unit cost of the packages
	per = 880;
	
	#Output text logic tree
	if amt < 0: 
		output = "  Invalid Input!";
	elif amt < 4: 
		cost = amt * per;
		output = "  No discount applied.\n  The total price to purchase {} packages is ${:,.2f}.".format(amt, cost);
	elif amt < 40: 
		cost = amt * per * 0.9;
		output = "  10% discount applied.\n  The total price to purchase {} packages is ${:,.2f}.".format(amt, cost);
	elif amt < 200: 
		cost = amt * per * 0.85;
		output = "  15% discount applied.\n  The total price to purchase {} packages is ${:,.2f}.".format(amt, cost);
	elif amt < 1000: 
		cost = amt * per * 0.7;
		output = "  30% discount applied.\n  The total price to purchase {} packages is ${:,.2f}.".format(amt, cost);
	else:
		cost = amt * per * (1 - 0.42); 
		output = "  42% discount applied.\n  The total price to purchase {} packages is ${:,.2f}.".format(amt, cost);
	
	#Print the output string to console
	print(output);

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
