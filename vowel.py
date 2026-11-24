word = input("Enter word: ")
count = 0
vowels='aeiouAEIOU'
for char in word:
    for count_of_vowel in vowels:
        if char == count_of_vowel:
            count+=1
print(count)

