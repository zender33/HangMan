from PoleDraw import PoleDrawing
from text import TextGeneration
from Intro import Intro


class HangMan(PoleDrawing, TextGeneration, Intro):

    def __init__(self):
        PoleDrawing.__init__(self)
        TextGeneration.__init__(self)
        Intro.__init__(self)
        self.wrong_guesses = 0
        self.wordpick = ''
        self.masked_word = []
        self.used_letters = []
        self.menu_choice = ''
        self.win = False

    def reset(self):
        self.wrong_guesses = 0
        self.wordpick = ''
        self.masked_word = []
        self.used_letters = []
        self.menu_choice = ''
        self.win = False


    def word_pick(self):
        import random

        words_file = open("words.txt", "r")
        words = [line.rstrip() for line in words_file]
        self.wordpick = random.choice(words)

    def word(self):

        self.word_pick()

        for i in self.wordpick:
            self.masked_word.append('_')

    def used_letters_tracking(self):
        s = 'Used Letters: '
        letters = ', '.join(self.used_letters)
        return 'Used Letters: ' + letters

    def lives(self, wrong_guesses):
        lives_string = 'Lives: ' + 'O ' * (6 - wrong_guesses) + 'X ' * wrong_guesses

        return lives_string

    def header(self, text, text2, width=117, padding=8):
        print(' ' * padding + '*'
              , text
              + text2.rjust(width - len(text) - 2, ' ')
              , '*')

    def intro(self):
        for j in self.logo_intro:
            self.display(j)

    def game_display(self):
        print('\n')
        self.draw_line()
        self.header(self.lives(self.wrong_guesses), self.used_letters_tracking())
        self.draw_line()
        self.display(self.text)
        self.draw(self.wrong_guesses)
        self.draw_line()
        a = 'The word consists of ' + str(len(self.wordpick)) + ' letters:'
        self.display(a)
        self.display(' '.join(self.masked_word))
        self.display(' ')
        self.draw_line()

    def intro_logo_draw(self):
        self.draw_line()
        self.intro()
        self.draw_line()

    def menu(self, scenario='new'):
        if scenario == "new":
            self.display("Are you ready to die cowboy!!!")
        elif scenario == "repeat":
            self.display('Do you dare to try again?!!!')
        self.display(' ')
        self.display('1. A real cowboy is never scared!')
        self.display('2. No! I am going home!')
        self.draw_line()
        a = input("What is your choice? ".rjust(78))

        self.menu_choice = a

        if self.menu_choice == '1':
            self.game()

        elif self.menu_choice == '2':

            print(4*'\n')
            self.draw_line()
            self.display(' ', reps=3)
            self.display('C H I C K E N !')
            self.display(' ')
            self.display('Bye, bye! Go to your mommy!')
            self.display(' ', reps=3)
            self.draw_line()
            exit()

        else:
                print(4 * '\n')
                self.draw_line()
                self.display(' ')
                self.display('Enter a valid choice! ')
                self.display(' ')
                self.draw_line()
                self.menu()

    def start(self):

        self.intro_logo_draw()
        self.menu()

    def game(self):
        self.word()
        print(self.wordpick)
        self.game_display()

        while self.wrong_guesses < 6 and self.win is False:

            letter_input = input('Please Enter a letter: '.rjust(78))

            if letter_input.upper() in self.used_letters:
                # print("You've already input this letter!")
                self.repeated()
                pass

            elif not letter_input.isalpha():
                # print("You've already input this letter!")
                self.invalid_input()
                pass

            elif self.wordpick.upper().find(letter_input.upper()) >= 0:
                self.right_guess()
                self.used_letters.append(letter_input.upper())
                for i in range(len(self.wordpick)):
                    if letter_input.upper() == self.wordpick[i].upper():
                        self.masked_word[i] = letter_input.upper()

                if self.wordpick.upper() == ''.join(self.masked_word).upper():
                    self.win = True

            else:
                self.wrong_guess()
                self.wrong_guesses = self.wrong_guesses + 1
                self.used_letters.append(letter_input.upper())

            self.game_display()

        if self.win == 1:

            print(4 * '\n')
            self.draw_line()
            self.display(' ', reps=2)
            self.display(' Y O U   W O N !')
            self.display(' ', reps=2)
            self.display(self.winning())
            self.display(' ', reps=4)
            self.draw_line()

        else:
            print(4 * '\n')
            self.draw_line()
            self.display(' ', reps=2)
            self.display(' G A M E   O V E R !')
            self.display(' ', reps=2)
            self.display(self.lost())
            self.display(' ')
            self.display('The word was: ' + self.wordpick)
            self.display(' ', reps=2)
            self.draw_line()

        self.reset()
        self.menu('repeat')

test = HangMan()


test.start()
print(test.wordpick)




