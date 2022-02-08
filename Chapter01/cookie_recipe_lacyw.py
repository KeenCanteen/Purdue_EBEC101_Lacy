"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 01.3 - cookie_recipe
Date: 02/07/2022

Description:
    Given a user's requested amount of cookies, this program calculates the required amounts of ingredients to make that many cookies

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
    #Inputs - prompt user for specific, floating point inputs
	num = int(input("How many cookies do you want to make? "));
	
	#Calculations - calculate ingredients required
	butter = num * 1.25 / 48;
	sugar = num * 1.5 / 48;
	flour = num * 2.5 / 48;
	
	#Output: output the ingredient list
	print("To make {:,d} cookies, you will need:".format(num));
	print("  {:>10,.2f} cups of butter".format(butter));
	print("  {:>10,.2f} cups of sugar".format(sugar));
	print("  {:>10,.2f} cups of flour".format(flour));


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
