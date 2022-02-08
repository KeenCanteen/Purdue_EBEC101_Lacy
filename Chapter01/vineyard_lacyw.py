"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 01.1 - vineyard
Date: 02/07/2022

Description:
    Describe your program here.

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
	print("Enter each of the following quantities in meters.");
	end_width = float(input("How wide is the end-post assembly? "));
	space = float(input("How much space should be between the vines? "));
	length = float(input("How long is this row? "));
	
	vines = int((length - 2 * end_width) / space);
	
	print("\nThere is enough space for {:.0f} vine(s) in this row.".format(vines));


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
