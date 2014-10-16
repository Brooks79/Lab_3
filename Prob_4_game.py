
# opens it as an open string
game = " "


# welcome for user to put name
name = raw_input("Please enter your name: ")
print ("\n")
print "Hello", name
print ("\n")
# the loop for the game
while game != "Y" or "Yes" or "y" or "yes":
	game = raw_input("Shall we play a game?: ")
	print ("\n")
	if game == "Y" or game == "Yes" or game == "y" or game == "yes":
		
		from turtle import *

		Q2 = int(raw_input("How many sides would you like your shape to have?: "))
		print ("\n")
		Q3 = int(raw_input("How long would you like each side to be?: "))
		print ("\n")
		Q4 = str(raw_input("What color would you like your shape to be?: "))
		print ("\n")
		Q5 = str(raw_input("What color would you like the background to be?: "))
		print ("\n")
		# which functions of "turtle" are being modified
		ninja = Pen()
		ninja.shape("turtle")
		ninja.screen.bgcolor(Q5)
		ninja.color(Q4)

		# this is what the turtle is doing
		for i in range(Q2):			
			ninja.forward(Q3)
			ninja.right(360/Q2)

	elif game == "N" or game == "n" or game == "No" or game == "no":
		print "Reformating C://... "
		print "Please Wait"
		print ("\n")
		import time
		time.sleep(5)

	else:
		print "Should have said yes"