user_choice = 1
total = 1
sum = 0
while (user_choice != -1):
	number = int(input("Enter a new integer: "))
	sum += number
	average = sum/total
	print("The running average is " , average);
	user_choice = int(input("Do you wish to continue ( Enter -1 to stop ): "))
	total += 1



