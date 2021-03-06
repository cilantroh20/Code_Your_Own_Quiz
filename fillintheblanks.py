#Easy Quiz - Ivy: Frank Ocean

easy_quiz_lyrics = "I thought that i was ____1___ when you said you __2__ me. It started from __3____. I had no chance to ___4___. I couldn't see you __5___." 

easy_song_spaces = ["____1___", "__2__ ", "__3____", "___4___", "__5___"]

easy_song_answers = ["dreaming", "loved", "nothing", "prepare", "coming"]

#Medium Quiz - Nights: Frank Ocean 

medium_quiz_lyrics = "Staying with you when I didn't have an __1___. Lovin on you when I didn't own a __2_____. Workin on a way to make it outta __3__. __4__ __5__."

medium_song_spaces = ["__1___","__2_____","__3__","__4__ ","__5__"]

medium_song_answers= ["address", "mattress", "texas", "every", "night"]

#Hard Quiz- Self Control- Frank Ocean 

hard_quiz_lyrics = "Now and then you miss it, sounds make you _1_. Some nights you dance with tears in your _2__. I came to visit cause you see me like a _3_. That's like never, cause i made you use your __4_ control. And you made me lose my __5_ control."

hard_song_spaces = ["_1_", "_2__", "_3_", "__4_", "__5_"]

hard_song_answers = ["cry", "eyes", "ufo", "self", "self"]

#This function will prompt the user to choose what level of they want 
#.strip is to take out the whitespaces
def choose_level():
	user_in = raw_input("What level of difficulty would you like? (easy, medium, hard)")
	if user_in.strip() == "easy":
		begin_quiz(easy_quiz_lyrics, easy_song_spaces, easy_song_answers)
	elif user_in.strip() == "medium":
		begin_quiz(medium_quiz_lyrics, medium_song_spaces, medium_song_answers)
	elif user_in.strip() == "hard":
		begin_quiz(hard_quiz_lyrics, hard_song_spaces, hard_song_answers)
	else:
		user_in = raw_input("Try again! (easy, medium, hard)")
		choose_level()
		
#this function begins the quiz and replaces the answers the user inputs
#prevents a user from making to many mistakes
#allows the user to choose to restart if they won or lost
#the input parameters are pre-defined in the choose_level() function
#they take a string of lyrics for each three levels(easy,medium,hard)
#they take two lists, which arespaces and answers for each level
def begin_quiz(quiz, spaces, answers):
	print quiz
	for count_spaces in range(0, len(spaces)):
		user_input = raw_input("What is" + spaces[count_spaces])
		attempts = 0
		max_attempts = 4	
		while user_input.lower().strip() != answers[count_spaces]:
			attempts += 1
			user_input = raw_input("That is incorrect, You're on your" + str(attempts) + "try. What is" + spaces[count_spaces] + "?")
			if attempts == max_attempts:
				print ("GAME OVER!")
				choose_level()
		else: 
			quiz = quiz.replace(spaces[count_spaces], answers[count_spaces])
			print("That is correct!" + quiz)
	if len(spaces) == len(answers):
		print ("CONGRATS!! YOU MADE IT!!")
		user_input= raw_input("Would like to play again? YES/NO")
		if user_input.lower().strip() == "yes": 
			choose_level()
		else:
			"Thanks, BYE!"

choose_level()
