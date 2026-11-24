numberss = 50
trials = 30
while(trials > 0) :
    number = int(input("Guess a number from 1 to 100: "))
    if(number == numberss) :
	    print("Congrats you won!!!")
	    trials = 0
    else :
	    trials -= 1
	    print("Wrong guess")
	    print("Number of attempts you have left are " , trials)
