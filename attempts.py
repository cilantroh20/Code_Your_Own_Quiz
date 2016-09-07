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
