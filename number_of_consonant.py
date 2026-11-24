vowel_counter = 0
vowel = "aeiou"
consonant_counter = 0
word = input("Enter any word to check the vowel and consonant: ")
for letters in word:
	if letters in vowel:
		vowel_counter += 1
	else:    
		consonant_counter += 1
	
	
print("The number of consonants in the word is ", consonant_counter )
print("The number of vowels int he word is ", vowel_counter )
