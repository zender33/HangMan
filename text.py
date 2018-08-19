
class TextGeneration:

    def __init__(self):
        self.text = ''

        self.right_guessing = ['Hell Yeah, b*tch!', 'Way to go!', 'If I keep going like that, I may actually survive'
            , 'Yuhuu', 'Damn I got lucky again', 'Phew! Got lucky again!', ]

        self.wrong_guessing = ['Oh shit, the end is coming', 'Noooo!!!', "I don't wanna die this way"
            , 'This is not how a cowboy is supposed to die', "A real cowboy never guesses right!"]

        self.repeated_input = ["Nice try, you've already tried this one", "Not this one again!",
                          "You've already tried this one", "Stop it with the cowboy tricks! You've used this one already!"]
        self.win_message = ['Congrats, Cowboy! You won', 'You won, motherf*cker!', 'A true cowboy never dies!']
        self.lost_message = ['R.I.P', 'May his lost soul rest in peace!', "He was a good cowboy, but never new his words"]
        self.invalid_message = ["Don't try to fool me, you filthy cowboy! Enter a valid input!"
            , "Hey! Does that look like a real letter to you?"
            , "Enter a real letter, you illiterate basterd before we hang you real quick!"
            , "Play like a real man! Enter a legit letter!"]


    def right_guess(self):
        import random
        self.text = random.choice(self.right_guessing)

    def invalid_input(self):
        import random
        self.text = random.choice(self.invalid_message)

    def wrong_guess(self):
        import random
        self.text = random.choice(self.wrong_guessing)
        return self.text

    def winning(self):
        import random
        self.text = random.choice(self.win_message)
        return self.text

    def lost(self):
        import random
        self.text = random.choice(self.lost_message)
        return self.text

    def repeated(self):
        import random
        self.text = random.choice(self.repeated_input)
        return self.text


# test = TextGeneration()
#
# test.wrong_guess()
#
# print(test.text)