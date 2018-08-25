import sqlite3


# Creates a database 'hangman_DB.db'
# with sqlite3.connect('hangman_DB.db') as conn:
#     c = conn.cursor()
#
# c.execute("""
# CREATE TABLE IF NOT EXISTS users(
# userID INTEGER PRIMARY KEY,
# username VARCHAR(25) NOT NULL,
# email VARCHAR(25) NOT NULL,
# name    VARCHAR(25) NOT NULL,
# family  VARCHAR(25) NOT NULL,
# sex     VARCHAR(25) NOT NULL,
# password VARCHAR(30) NOT NULL,
# played INTEGER,
# wins INTEGER,
# loses INTEGER
# );
# """)

import sqlite3


class Database:

    def register(self, name, family, username, email, password, sex):

        with sqlite3.connect('hangman_DB.db') as conn:
            c = conn.cursor()

        user_register =  ("""
                            INSERT INTO users (username, email, password, name, family,sex, played, wins, loses)
                            VALUES(?, ?, ?, ?, ?, ?, "0", "0", "0")""")
        c.execute(user_register,[(username), (email), (password), (name), (family), (sex)])
        conn.commit()

        conn.close()

    def fetch_data(self):
        with sqlite3.connect('hangman_DB.db') as conn:
            c = conn.cursor()

        conn.commit()

        c.execute("""
        SELECT * FROM users
        """)

        print(c.fetchall())
        conn.close()

    def login(self, username, password):
        # while True:

            with sqlite3.connect('hangman_DB.db') as conn:
                c = conn.cursor()

            user_identify = ("SELECT * FROM users WHERE username = ? AND password = ?")
            c.execute(user_identify, [(username), (password)])
            result_login_menu = c.fetchall()
            return result_login_menu

    def update_wins(self, user, score):
        with sqlite3.connect('hangman_DB.db') as conn:
            c = conn.cursor()

        new_score = score

        c.execute("""
            UPDATE users
            SET wins = "{}"
            WHERE username = "{}"
            """.format(new_score, user))

        conn.commit()
        conn.close()

            # if result:
            #     for i in result:
            #         print('Welcome,', i[2], i[3])
            #
            #     return ('exit')
            #
            # else:
            #     print('Wrong Username or password')
            #     again = input("Try again(y/n): ")
            #
            #     if again.lower() == 'n':
            #         print("BYE!!!")
            #         exit()

    def update_times(self, user, score):
        with sqlite3.connect('hangman_DB.db') as conn:
            c = conn.cursor()

        new_score = score

        c.execute("""
            UPDATE users
            SET played = "{}"
            WHERE username = "{}"
            """.format(new_score, user))

        conn.commit()
        conn.close()

    def update_loses(self, user, score):
        with sqlite3.connect('hangman_DB.db') as conn:
            c = conn.cursor()

        new_score = score

        c.execute("""
            UPDATE users
            SET loses = "{}"
            WHERE username = "{}"
            """.format(new_score, user))

        conn.commit()
        conn.close()

    def highscores_fetch(self):
        with sqlite3.connect('hangman_DB.db') as conn:
            c = conn.cursor()

        c.execute("""
            SELECT username, wins
            FROM users
            ORDER BY wins DESC
            LIMIT 10;
        """)
        hs = c.fetchall()

        conn.close()
        return hs

    def player_stats(self, username):

        with sqlite3.connect('hangman_DB.db') as conn:
            c = conn.cursor()

        user_register =  ("""
                            SELECT username, played, wins, loses FROM users WHERE username = ?;
                         """)
        c.execute(user_register, [(username)])

        prt = c.fetchall()
        conn.close()
        return prt


# t = Database()

