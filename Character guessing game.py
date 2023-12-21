import random

def choose_word():
    fruits = ["apple","banana","mango","orange","grapes","pineapple","watermelon","papaya","guava","pomegranate"]
    print("\nGuess a character:",end=" ")
    select_word = random.choice(fruits)
    for i in select_word:
        print("_",end=" ")
    print()
    return select_word

def word_game(word):
    chance = len(word)+4
    guessing_words = ''
    while chance != 0:
        user_guess = input("\nGuess a character:").lower()
        if len(user_guess) >1 or not user_guess.isalpha():
            print("You must enter a single letter and alphabets")
        elif user_guess in word:
            if user_guess in guessing_words:
                print("This letter is already placed")
            else:
                counts = word.count(user_guess)
                for k in range(counts):
                    guessing_words += user_guess
                display = ''
                for char in word:
                    if char in guessing_words:
                        display += char
                    else:
                        display += "_"
                print(display)
                if display == word:
                    print('Congratulations, You won!')
                    break
        else:
            chance -= 1
            print("Guessing character is wrong, you have",chance,"chance only")
            if chance == 0:
                print("*You lose*")
                print("Correct word is",word)

print('\tGuess the word! HINT: word is a name of a fruit')
word = choose_word()
print(word_game(word))

