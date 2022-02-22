"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 03.2 - Sum Average
Date: 02/21/2022

Description:
    This program receives some number of inputs and tells the user their sum and average as well as the number of numbers input

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
	
	#Initialize some variables
	nums = [];
	numnums = 0;
	inNum = 0;
	sum = 0;
	
	#Prompt user until they tell us to stop
	while inNum >= 0:
		inNum = float(input("Enter a non-negative number (negative to quit): "));
		#Break statment to correct and off-by-one error
		if(inNum < 0):
			break;
		nums = [nums, inNum];
		numnums += 1;
		sum += inNum;
	
	#Compute Average
	avg = sum / numnums;
	
	#Conditional for if the user input no numbers
	if(numnums == 0):
		print("  You didn't enter any numbers.");
	else:
		print("  You entered {:.0f} numbers.".format(numnums));
		print("  Their sum is {:.3f} and their average is {:.3f}.".format(sum, avg));
	



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
