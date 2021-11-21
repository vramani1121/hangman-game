import random
import re
class Hangman:
    def __init__(self , wordlist):
        self.wordlist = wordlist
        self.attempts_remain = 6
        self.current_letter = ''
        self.chosen_word = ''
        self.guessed_letters = []

    def choose_the_word(self):
        file = open(self.wordlist)
        words = file.read().split('\n');
        word_cnt = len(words)
        self.chosen_word = words[random.randrange(0 , word_cnt)]
        self.word_status = ['_' for i in range(len(self.chosen_word))]

    def fill_word_status(self):
        nos = random.randrange(1,3)
        for i in range(nos):
            position = random.randrange(0 , len(self.chosen_word))
            self.word_status[position] = self.chosen_word[position]

    def guess_the_letter(self):
        letter=input("guess the letter")
        if (letter in self.guessed_letters):
            print("you have already guessed that letter : {}".format(self.guessed_letters))
            return
        self.guessed_letters.append(letter)
        occurences=[]
        occurence=re.finditer(letter,self.chosen_word)
        for m in occurence:
            occurences.append(m.start())

        if(len(occurences) == 0):
            self.attempts_remain -= 1
            print("oops!wrong guess . attempts remaining is {}".format(self.attempts_remain))
        else:
            for position in occurences:
                self.word_status[position] = self.chosen_word[position]
            print("yap , correct letter")

    def get_word_status(self):
        print("current status : {} \n ".format(' '.join(self.word_status)))