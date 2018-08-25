
class TextGeneration:

    def __init__(self):
        self.text = ''

    def start_game(self):
        self.text = 'Good Luck'

    def right_guess(self, letter):
        import random

        right_guessing = ['{} has been always been my favourite letter'.format(letter.upper())
                            , 'I love {}'.format(letter.upper())
                            , 'If I keep going like that, I may actually survive'
                            , 'I knew it!'
                            , 'Damn I got lucky again'
                            , 'Phew! Got lucky again!'
                            , '{}, What a great letter'.format(letter.upper())]
        self.text = random.choice(right_guessing)

    def invalid_input(self, letter):
        import random

        invalid_message = ["Enter a valid input!"
            , "{}!?! Does that look like a real letter to you?".format(letter.upper())
            , "Really!?! {} ??? Is that a new letter?".format(letter.upper())
            , "Play like a real man! Enter a legit letter! Not things like {}!".format(letter.upper())]

        self.text = random.choice(invalid_message)

    def wrong_guess(self, letter):
        import random

        wrong_guessing = ['The end is coming'
                            , '{} ?!? Why??? Noooo!!!'.format(letter.upper())
                            , "Never liked the Letter {}".format(letter.upper())
                            , 'This is not how a cowboy is supposed to die'
                            , "That's weird. A letter without {}".format(letter.upper())
                          ]

        self.text = random.choice(wrong_guessing)
        return self.text

    def winning(self):
        import random

        win_message = ['Congrats! You won'
                            , 'You won!'
                            , 'A true cowboy never dies!']

        self.text = random.choice(win_message)
        return self.text

    def lost(self):
        import random
        lost_message = ['R.I.P'
                        , 'May his lost soul rest in peace!'
                        ]
        self.text = random.choice(lost_message)
        return self.text

    def repeated(self,letter):
        import random

        repeated_input = ["Nice try, you've already tried {}".format(letter.upper())
                                , "Not {} again!".format(letter.upper())
                                , "You've already tried {}".format(letter.upper())
                                , "How many time are you gonna try {}".format(letter.upper())
                              ]
        self.text = random.choice(repeated_input)
        return self.text


# test = TextGeneration()
#
# test.wrong_guess()
#
# print(test.text)