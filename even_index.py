user_word = input("Enter a word: ")

counter = 1
for letter in user_word:
    if counter % 2 == 0:
        print(letter)
    counter += 1
