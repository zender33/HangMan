class PoleDrawing:

    def __init__(self):
        self.pole_template = [
            "_______  ",
            "|/    |  ",
            "|        ",
            "|        ",
            "|        ",
            "|        ",
            "======== ",
            "|      | "
        ]

    def display(self, text, width=117, padding=8, reps=1):

        for i in range(reps):
            text_display = ' ' * padding + '*' + text.center(width, ' ') + '*'
            print(text_display)

    def draw_line(self, width=60, padding=8):
        print(' ' * padding + '* ' * width)

    def HangManReset(self):
        self.pole_template = [
            "_______  ",
            "|/    |  ",
            "|        ",
            "|        ",
            "|        ",
            "|        ",
            "======== ",
            "|      | "
        ]

    def hanging(self, line, index, symbol):

        l = []
        for i in self.pole_template[line]:
            l.append(i)
        l[index] = symbol
        new_line = ''.join(l)
        self.pole_template[line] = new_line

    def pole_conditions(self, wrong_guess):

        if wrong_guess == 0:
            self.HangManReset()

        elif wrong_guess == 1:
            self.hanging(2, 6, '0')

        elif wrong_guess == 2:
            self.hanging(3, 6, '|')

        elif wrong_guess == 3:
            self.hanging(3, 5, '/')

        elif wrong_guess == 4:
            self.hanging(3, 7, '\ ')

        elif wrong_guess == 5:
            self.hanging(4,5,'/')

        elif wrong_guess == 6:
            self.hanging(4, 7, '\ ')

    def draw(self, x):

        for i in range(x+1):
            self.pole_conditions(i)

        for j in self.pole_template:
            self.display(j)

        # self.draw_line()


# test = PoleDrawing()
# test.display('Hello', reps=10)
# print('newline')

