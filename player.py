import creator
hangman = creator.Hangman('wordlist.txt')
hangman.choose_the_word()
hangman.fill_word_status()

while True:
    hangman.get_word_status()
    hangman.guess_the_letter()
    if(hangman.attempts_remain == 0):
        print("out of attempts . the word was [{}]. ".format(hangman.chosen_word))
        print("Now, your game is over!")
        break
    elif(hangman.chosen_word == ''.join(hangman.word_status)):
        print("hurray! you won the game")
        print("The word is [{}].".format(hangman.chosen_word))
        break