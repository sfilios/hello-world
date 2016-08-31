print "Welcome to the spaceship Voltreon. You have 10 minutes to escape before aliens who \
have boarded the ship find you."


print "You see 3 doors from the control room, labeled 1, 2, a nd 3. Which do you enter?"

door = raw_input("> ")

if door == "1":
	print "you find an alien waiting for his friends, looking grumpy"
	print "1. Kick him while he isn't looking"
	print "2. Run away fast"
	
	alien= raw_input(">")
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
		print "The aliens see you and catch you. They make you listen to alien music. It's not that bad."
	else: 
		print "The aliens don't like that. They zap you with lasers."
elif door == "2":
	print "oh snap, it's locked. They aliens come in through door one and capture you."
elif door =="3":
	print "You find a lunchbox and try to open it. It forms a black hole when you do, and everyone is sucked in."
else:
	print "That's not really an option at this point."
