while True:
	import random
	list = ["rock", "paper", "scissors"]

	Computer = random.choice(list)
	Player = None

	while Player not in list:
		Player = input("Choose rock, paper or scissors?: ").lower()

	print("Computer chooses: "+Computer)
	print("Player choice: "+Player)

	if Player == Computer:
		print("It's a Tie!!")
	elif Player == "rock":
		if Computer == "paper":
			print("You lose!")
		if Computer == "scissors":
			print("You Win!")
	elif Player == "scissors":
		if Computer == "rock":
			print("You lose!")
		if Computer == "paper":
			print("You Win!")
	elif Player == "paper":
		if Computer == "scissors":
			print("You lose!")
		if Computer == "rock":
			print("You Win!")
	
	playagain = input("Play again? (yes/no): ").lower
	if playagain != "yes":
		break

print("Goodbye")