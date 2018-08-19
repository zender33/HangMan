class Display:

    def display(self, text, width=117, padding=8):
            print(' ' * padding + '*' + text.center(width, ' ') + '*')

    def draw_line(self, width=60, padding=8):
        print(' ' * padding + '* ' * width)

