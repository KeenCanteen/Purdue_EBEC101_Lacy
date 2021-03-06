"""
Author: William Rhodes Lacy, lacyw@purdue.edu
Assignment: 03.3- Rainfall
Date: 02/21/2022

Description:
    This program (tediously) gathers rainfall data from the user then computes total and average rainfall

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

	years = 0;
	
	
	while years <= 0:
		years = int(input("Enter the number of years: "));
		if years <= 0:
			print("Invalid input; years must be greater than 0.");
			
	sum = 0;
	months = 12 * years;
	cal = ["Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."];
	
	for year in range(1, years+1):
		print("  For year No. {}".format(year));
		for month in cal:
			moData = -1;
			while moData < 0:
				moData = float(input("    Enter the rainfall for " + month + ": "));
				if moData <0:
					print("    Invalid input; rainfall cannot be negative.");
			sum += moData
	
	avg = sum / months;
	
	print("There are {} months.".format(months));
	print("The total rainfall was {:.2f} inches.".format(sum));
	print("The monthly average rainfall was {:.2f} inches.".format(avg));

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
