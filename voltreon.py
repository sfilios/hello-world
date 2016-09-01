from sys import exit


def control_room(t,s):
	print "What do you want to do? "
	print "1. examine console"
	print "2. open door one"
	print "3. open door two"

	dec = raw_input("> ")

	if dec == "1":
		print "you examine the control console, and notice that only the button controlling the airlock has power"
		timer(t)
		print "do you push the button? (Y/N)"
		button=raw_input("> ")
		
		if button == "Y":
			aliens=button_press(s)
		elif button =="N":
			print "Ok, well you know what's there."
			control_room(t,s)
		else:
			print "that's not really an option"
			control_room(t,s)

	elif dec == "2":
		escape_room(t,s)
	elif dec =="3":
		s=closet()
		control_room(t,s)
	else:
		print "That's a bad idea."
		control_room(t,s)

def closet():
	print "my goodness! It's just a closet with a spacesuit in it! Let's put this on"
	return True

def escape_room(t, s):

	if aliens_alive(s) == True:	
		print "you find an alien waiting for his friends, looking grumpy"
		print "1. Kick him while he isn't looking"
		print "2. Run away fast"
		timer(t)
		alien = raw_input(">")

		if alien == "1":
			print "You hurt him pretty bad. And look, he was guarding the escape hatch!"
			print "Do you want to leave?"
			print "1. Yes"
			print "2. No" 
			leave = raw_input("> ")

			if leave == "1":
				print "Congratulations! You escaped!"
			else:
				print "You shouldn't have dawdled. The aliens find you and wear you as a coat."

		elif alien =="2":
			print "you go back to the control room"
			timer(t)
			control_room(t,s)

	elif aliens_alive(button) == False:
		print "You find a dead alien on the ground. He was guarding the escape hatch!"
		print "Do you want to leave? (Y/N)"
		leave = raw_input("> ")		
		if raw_input == "Y":
			print "You escaped! You're a winner!"
		elif raw_input =="N":
			print "I don't think that's a good idea."
			escape_room(t, button)

def button_press(s):
	if s == True:
		print "You opened the airlock and killed all the aliens"
		print "Great job!"
		
	else:
		print "you opened the airlock and killed all the aliens! But you died too."	
		exit(0)


def timer(t):
	t=t-1
	print "you know have %d minutes" %t
	return t


def aliens_alive(button):
	if button == True:
		return False
	else:
		return True


def start():
	print "Welcome to the spaceship Voltreon. You have 10 minutes to escape before aliens"
	print "have boarded the ship find you."
	time = 10
	spacesuit=False
	print "Time remaining is %d minutes" %time
	aliens=True
	print "You see 2 doors from the control room, labeled 1 and 2. You also see a control console"
	control_room(time,spacesuit)

start()
