import random

words_list = ["python", "java", "kotlin", "javascript"]
print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit: ')
if menu == "exit":
    exit()
print()
chosen_word = random.choice(words_list)
word = '-' * len(chosen_word)
print(word)
answer = list(word)
mistake = 0
used_letters = []
while mistake != 8:
    letter = input('Input a letter: ')
    if len(letter) != 1:
        print("You should input a single letter")
    elif used_letters.count(letter) > 1:
        print("You already typed this letter")
    elif letter.isupper() or letter.isalpha() is False:
        print("It is not an ASCII lowercase letter")
    elif letter in used_letters:
        print("You already typed this letter")
    # if letter in answer and chosen_word and letter != "-":
    #    print('No improvements')
    #      mistake += 1
    elif letter in chosen_word:
        used_letters.append(letter)
        for i in range(len(chosen_word)):
            if letter == chosen_word[i]:
                answer[i] = letter
    else:
        print('No such letter in the word')
        mistake += 1
        used_letters.append(letter)

    if mistake < 8:
        print()
        print(''.join(answer))
    else:
        print('You are hanged!')
    if '-' not in answer:
        print("You guessed the word " + chosen_word + "! \nYou survived!")
        break
