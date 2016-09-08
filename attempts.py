def check_answer(answer_list,q,attempts,answer_index): #17 lines long
        # q is the adjusted list of question_blank to make sure that the correct questions are replaced.
        # attempts is the number of trys before failure.
        # answer_index is the spot that the correct answer should be in the list of Answers.
        index = 1
        while index <= attempts:
                left = attempts - index
                guess = raw_input("What is your guess for " + str(q[0]) +"?  ")
                if guess not in answer_list and left != 0:
                        print "You have guessed incorrectly.  You have " + str(left) + " attempts left."
                else:
                        if guess == answer_list[answer_index]:
                                #Checks to see if the guess is indeed at the correct space in the answer list
                                print "You are correct."
                                return guess
                        elif index < attempts:
                                print "Close but no cigar"
                                print "You have guessed incorrectly.  You have " + str(left) + " attempts left."
                index = index + 1
        return False
