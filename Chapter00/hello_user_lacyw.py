"""
Author: Your Name, lacyw@purdue.edu
Assignment: 00.1 - Hello User
Date: 01/31/2022

Description:
    A basic greeting that says hello and repeats the inputted string back to the user.

Contributors:
    Name, lacyw@purdue.edu 

My contributor(s) helped me:
    [N/A] understand the assignment expectations without
        telling me how they will approach it.
    [N/A] understand different ways to think about a solution
        without helping me plan my solution.
    [N/A] think through the meaning of a specific error or
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

#The main function
def main():
	#Prompt user for input
	name = input('What is your name? ');
	#Say hello
	print('Hello ', name, '!', sep='')
	
if __name__ == "__main__":
    main()