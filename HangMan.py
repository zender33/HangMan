from PoleDraw import PoleDrawing
from text import TextGeneration


class HangMan(PoleDrawing, TextGeneration):
    def __init__(self):
        PoleDrawing.__init__(self)
        TextGeneration.__init__(self)

        self.name = ''
        self.family = ''
        self.username = ''
        self.sex = ''
        self.wins = 0
        self.loses = 0
        self.times = 0
        self.email = ''

        self.him_her = ''
        self.he_she = ''
        self.boy_girl = ''
        self.cowboy_cowgirl = ''
        self.be_with = ''
        self.be_him_her = ''

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

    def game(self):
        self.word()
        print(self.wordpick)
        self.start_game()
        self.game_display()

        while self.wrong_guesses < 6 and self.win is False:

            letter_input = input('Please Enter a letter: '.rjust(78))

            if letter_input.upper() in self.used_letters:
                # print("You've already input this letter!")
                self.repeated(letter_input)
                pass

            elif not letter_input.isalpha():
                # print("You've already input this letter!")
                self.invalid_input(letter_input)
                pass

            elif self.wordpick.upper().find(letter_input.upper()) >= 0:
                self.right_guess(letter_input)
                self.used_letters.append(letter_input.upper())
                for i in range(len(self.wordpick)):
                    if letter_input.upper() == self.wordpick[i].upper():
                        self.masked_word[i] = letter_input.upper()

                if self.wordpick.upper() == ''.join(self.masked_word).upper():
                    self.win = True

            else:
                self.wrong_guess(letter_input)
                self.wrong_guesses = self.wrong_guesses + 1
                self.used_letters.append(letter_input.upper())

            self.game_display()

# test = HangMan()
# test.start()





