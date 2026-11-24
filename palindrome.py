word = input("Enter any word to check if it's a palindrome word: ");
reverseWord = ""
for character in word :
	reverseWord = character + reverseWord

if (reverseWord ==  word):
    print("It is a a palindrome")

else :
    print("It is not  a palindrome")

