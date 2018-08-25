# from PoleDraw import PoleDrawing
from HangMan import HangMan
from database import Database
import time


class Menu(HangMan, Database):

    def __init__(self):
        HangMan.__init__(self)
        Database.__init__(self)
        self.logo_intro = ["  _   _            __    __  ________  __    __            __    __"

            , " | | | |    /\    |  \  | | /   _____||  \  /  |    /\    |  \  | |"

            , " | |_| |   /  \   |   \ | ||   / ___  |   \/   |   /  \   |   \ | |"

            , " |  _| |  / /\ \  | |\ \| ||  |  \  \ | |\  /| |  / /\ \  | |\ \| |"

            , " | | | | /  ==  \ | | \   ||   \__|  || | \/ | | /  ==  \ | | \   |"

            , " |_| |_|/_/    \_\|_|  \__| \________/|_|    |_|/_/    \_\|_|  \__|"
            , "                                                                   "

            , "                                                                   "

            # , "___________________________________________________________________"

            , "Copyright(c) 2018          Martin Ivanov          Release v 2.0"

            , "___________________________________________________________________"

            , "                          "
                           ]

        self.story = []

        self.user_details = []

    def start_menu(self):

        while True:
            self.draw_line()
            for i in self.logo_intro:
                self.display(i)
                time.sleep(0.05)
            self.draw_line()

            self.display('S T A R T  M E N U')
            self.display('------------------')
            self.display("1. LOGIN             ")
            self.display("2. REGISTER          ")
            self.display("3. FORGOTTEN PASSWORD")
            self.display("4. EXIT              ")

            self.draw_line()

            input_start_menu = input("Enter your choice: ".rjust(78))

            if input_start_menu == '1':

                # user_details = self.login_menu()
                self.login_menu()

            elif input_start_menu == '2':
                self.register_menu()

            elif input_start_menu == '3':
                print(' ')
                self.draw_line()
                self.display('')
                self.display('----------------------------------')
                self.display('U N D E R  C O N S T R U C T I O N')
                self.display('----------------------------------')
                self.display(' ')
                self.draw_line()

                tem_menu = input('Press Enter to return to the Start Menu'.rjust(88))
                self.start_menu()

            elif input_start_menu == '4':
                self.exit_display('start')

            else:
                print("Enter a valid input")

    def login_menu(self):
        print(' ')
        self.draw_line()
        self.display('L O G  I N')
        self.display('----------')

        while True:
            self.draw_line()
            username = input('Please enter your username: '.rjust(81))
            password = input('Please enter your password: '.rjust(81))
            self.draw_line()
            result = self.login(username, password)
            self.user_details = result

            if result:
                for i in result:
                    print('')
                    self.draw_line()
                    self.display('Welcome, {} {}'.format(i[3], i[4]))
                    self.draw_line()

                self.user_details_update()
                self.main_menu()




            else:
                print('\n')
                self.draw_line()
                self.display('Wrong Username or password')
                self.display('--------------------------')
                self.display('Do you want to go back to the start menu')
                self.draw_line()

                again = input("(y/n): ".rjust(70))

                if again.lower() == 'y':
                    self.start_menu()

    def register_menu(self, rjust=71):
        print(' ')
        self.draw_line()
        self.display('S I G N  U P')
        self.display('------------')
        self.draw_line()

        name = input('First Name: '.rjust(rjust))
        family = input('Last Name:  '.rjust(rjust))
        username = input('Username:   '.rjust(rjust))
        email = input('Email:      '.rjust(rjust))
        password = input('Password:   '.rjust(rjust))

        while True:
            sex = input('Sex(m/f):   '.rjust(rjust))

            if sex in ['m','f']:
                break

            else:
                print(' ')
                self.draw_line()
                self.display("Enter  'm' or 'f'")
                self.draw_line()
                print(' ')

        self.register(name, family, username, email, password, sex)

        print(' ')
        self.draw_line()
        self.display("Thank you for registering, {}".format(name))
        self.draw_line()
        print(' ')

    def main_menu(self):

        while True:
            print(' ')
            self.draw_line()
            self.display('M A I N  M E N U')
            self.display('----------------')
            self.display("1. Play        ")
            self.display("2. Player Stats")
            self.display("3. High Scores ")
            self.display("4. Exit        ")
            self.draw_line()

            input_main_menu = input("Enter your choice: ".rjust(78))

            if input_main_menu == '1':

                self.play()

            elif input_main_menu == '2':
                self.user_stats_menu()
                self.main_menu()

            elif input_main_menu == '3':
                self.highschore_menu()
                self.main_menu()

            elif input_main_menu == '4':
                self.exit_display('main')

    def user_details_update(self):

        self.username = self.user_details[0][1]
        self.email = self.user_details[0][2]
        self.name = self.user_details[0][3]
        self.family = self.user_details[0][4]
        self.sex = self.user_details[0][5].lower()
        self.times = int(self.user_details[0][7])
        self.wins = int(self.user_details[0][8])
        self.loses = int(self.user_details[0][9])

    def highschore_menu(self):

        highscores = self.highscores_fetch()
        self.draw_line()
        self.display(' ')
        self.display('H I G H  S C O R E S')
        self.display('--------------------')
        self.display(' ')

        for i in range(len(highscores)):
            y = str(i+1)+'.'+str(highscores[i][0]) + str(' '*(20 -len(highscores[i][0])))+ ' '+ str(' '*3)+str(highscores[i][1])


            self.display(y)
        self.display(' ')
        self.draw_line()
        a = input("Please press enter to go back to the main menu".rjust(90))

    def user_stats_menu(self):

        self.gen_story()

        user_starts_list = self.player_stats(self.username)

        print('\n')
        self.draw_line()
        self.display(' ')
        self.display('P L A Y E R  S T A T S')
        self.display('----------------------')
        self.display(' ')
        self.display('{} played {} times. From those {} times, {} won {} and lost {} times.'
                     .format(
                               user_starts_list[0][0], user_starts_list[0][1]
                             , user_starts_list[0][1], self.he_she
                             , user_starts_list[0][2], user_starts_list[0][3]
                             )
                     )
        self.display(' ')
        self.draw_line()

        a = input("Press enter to return to the Main Menu".rjust(85))

    def exit_display(self, menu_type = 'start'):

        print('\n')
        self.draw_line()
        self.display('')
        if menu_type == 'main':
            self.display("GOOD BYE, {}".format(self.username.upper()))
        elif menu_type == 'start':
            self.display("G O O D  B Y E")
        self.display('')
        self.draw_line()
        time.sleep(2)
        exit()

    def gen_story(self):

        if self.sex == 'm':
            self.him_her = 'him'
        elif self.sex == 'f':
            self.him_her = 'her'

        if self.sex == 'm':
            self.he_she = 'he'
        elif self.sex == 'f':
            self.he_she = 'she'

        if self.sex == 'm':
            self.cowboy_cowgirl = 'cowboy'
        elif self.sex == 'f':
            self.cowboy_cowgirl = 'cowgirl'

        if self.sex == 'm':
            self.be_with = 'girls'
        elif self.sex == 'f':
            self.be_with = 'boys'

        if self.sex == 'm':
            self.be_him_her = 'boys'
        elif self.sex == 'f':
            self.be_him_her = 'girls'

        self.story = ['In the wild west, there was a {}, named {}'.format(self.cowboy_cowgirl, self.name)
            , 'A very, very bad {}'.format(self.cowboy_cowgirl)
            , 'Some called {} {}'.format(self.him_her, self.username)
            , 'Everyone knew {}'.format(self.him_her)
            , 'All the {} wanted to be {}'.format(self.be_him_her, self.him_her)
            , "All the {} wanted to be with {}".format(self.be_with, self.him_her)
            , ''
            , 'One unfortunate day, after another bank robbery, the notorious {} {} was finally captured'.format(self.cowboy_cowgirl, self.name)
            , 'The Sherriff told {}:'.format(self.name)
            , "'{}, Today is your lucky day,!' ".format(self.username.capitalize())
            , "'If you guess my word, I will let you go,'"
            , "'else you die!'"
                      ]

    def game_end(self):

        self.times = self.times + 1

        self.update_times(self.username, self.times)

        if self.win == 1:

            self.wins = self.wins + 1

            self.update_wins(self.username, self.wins)

            print(4 * '\n')
            self.draw_line()
            self.display(' ', reps=2)
            self.display(' Y O U   W O N !')
            self.display(' ', reps=2)
            self.display(self.winning())
            self.display(' ', reps=4)
            self.draw_line()
            print('This is win #{}'.format(self.wins))
            print('out of {} plays'.format(self.times))

        else:
            self.loses = self.loses + 1

            self.update_loses(self.username, self.loses)

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
            print('This is lose #{}'.format(self.loses))
            print('out of {} plays'.format(self.times))

        self.reset()

        self.main_menu()

    def play(self):

        self.gen_story()

        # print(self.username, self.name, self.family, self.sex)

        print(' ')
        self.draw_line()
        self.display(' ')

        for i in self.story:
            self.display(i)
            time.sleep(0.5)  #TO CHANGE TO 0.5-1sec
        self.display(' ')
        self.draw_line()

        while True:
            choice_play = input("'Do you want to play! (y/n): ".rjust(82))

            if choice_play.lower() == 'y':
                self.game()

            elif choice_play.lower() == 'n':
                print(' ')
                self.draw_line()
                self.display('And then {} got hanged'.format(self.name))
                self.draw_line()

                self.main_menu()
            else:
                self.display("Please enter valid input 'y' or 'n'")

            self.game_end()


HangMan_Game = Menu()
HangMan_Game.start_menu()
