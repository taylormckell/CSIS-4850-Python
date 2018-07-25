# Taylor Cella
# Final Number Game Assignment
import random
import logging
import optparse

fh = logging.FileHandler("gamewarningLog.log")  # Creates our file handler
fh.setLevel(logging.WARNING)  # sets to warning and above

sh = logging.StreamHandler()  # Creates our stream handler
sh.setLevel(logging.DEBUG)

logger = logging.getLogger()  # Creates a logger
logger.setLevel(logging.DEBUG)

logger.addHandler(fh)  # Adds the file handler to our logger
# If you comment this line below, all logging warnings will no longer be printed to the console.
# logger.addHandler(sh)

try:

    def login(u_name, p_word):
        """Start menu: Lets users login or quit"""

        file_name = 'user_list.txt'
        user_list = {}

        file = open(file_name)
        line = file.readline()
        logger.debug("Our user-file list was opened and read.")
        while line:
            logger.debug("Each line is being stripped of the '\ n ' character")
            index = line.rstrip("\n")
            line = file.readline()
            logger.debug("The password is being set as the value to the username as the key")
            user_list[index] = line.rstrip("\n")
            line = file.readline()
        file.close()

        logger.debug("Iterating through the list of keys and values in the user_file dictionary")
        for k, v in user_list.items():
            if u_name in user_list.keys():
                logger.debug("Checking to see if the username provided is in the dictionary")
                dict_index = user_list.get(u_name)
                logger.debug("Checking to see if the password provided is in the dictionary")
                if p_word == dict_index:
                    print("Welcome to the game, " + u_name + "!")
                    game_play()
                    logger.debug("Since the input is valid, now leaving to go to the game_play() function")
                elif v != p_word:
                    logger.debug("If the password is not in the dictionary, then users will be able to try again.")
                    attempts = 0
                    b = True
                    while b:
                        logger.debug("Only three password attempts are allowed")
                        while attempts <= 3:
                            new_pass = input("That password is incorrect. Please enter it again. ")
                            if dict_index == new_pass:
                                logger.debug("If the password is correct, will go to the game_play() function.")
                                print("That is correct, " + u_name + " welcome to the game!")
                                game_play()
                            logger.debug("Updates the attempts to make sure no more than 3 are allowed")
                            attempts += 1
                        if attempts > 3:
                            logger.debug("Prevents those with the wrong password from playing the game.")
                            print("I'm sorry, that's too many attempts. You are locked from the system.")
                            quit()
            else:
                logger.debug("If the username is not found, then the option of creating a new account is given.")
                logger.debug("Moving to the new_account() function.")
                print("I'm sorry, that username is not found.")
                new_account()


    def new_account():
        """Allows for the creation of a new account"""
        file_name = 'user_list.txt'
        user_list = {}

        file = open(file_name)
        line = file.readline()
        logger.debug("Our user-file list was opened and read.")
        while line:
            logger.debug("Each line is being stripped of the '\ n ' character")
            index = line.rstrip("\n")
            line = file.readline()
            logger.debug("The password is being set as the value to the username as the key")
            user_list[index] = line.rstrip("\n")
            line = file.readline()
        file.close()

        logger.debug("Asks the users if they would like to create an account.")
        reg_user = input("Would you like to create an account to play the game? ")
        a = True
        while a:
            if reg_user.lower() == "yes":
                new_user = input("Please enter a username. ")
                logger.debug("Creates a new username to be input into the list")
                logger.debug("Valid input would be two passwords that are the same.")
                if new_user in user_list.keys():
                    print("I'm sorry, that username already exists. Please try again. ")
                else:
                    final_user = new_user

                b = True
                while b:

                    new_pass = input("Now, please enter a password. ")
                    confirm_pass = input("Please type in your password again for confirmation. ")

                    logger.debug("Valid input must be a username that is not already within the users list.")
                    # for k, v in user_list.items():

                    if new_pass == confirm_pass:
                        logger.debug("If the new passwords match, then they are saved to a final password variable.")
                        final_pass = new_pass
                        b = False

                    if new_pass != confirm_pass:
                        logger.debug("Valid input must have matching passwords.")
                        print("I'm sorry, your passwords don't match. Please try again.")

                new_users = {final_user: final_pass}
                user_list.update(new_users)
                print(user_list)
                logger.debug("The user-list text file is now updated with the new user account.")
                with open(file_name, 'a') as f:
                    f.writelines(final_user + "\n")
                    f.writelines(final_pass + "\n")
                logger.debug("Program now moves to the game_play() function.")
                game_play()

            elif reg_user.lower() == "no":
                logger.debug("If the user says no, the program should quit.")
                print("See you next time!")
                quit()
            else:
                logger.debug("Valid input must be yes or no.")
                logger.warning("This is invalid input.")
                reg_user = input("Please enter either yes or no. ")


    def game_play():
        """Where the users decide which level they will want to play"""
        a = True
        while a:
            logger.debug("We are now in the 'game_play' function.")
            logger.debug("Valid input must be 1, 2, or 3.")
            try:
                level = int(input("Which level would you like to play? Level 1, 2, or 3? "))
                if level == 1:
                    level_one()
                    a = False
                elif level == 2:
                    level_two()
                    a = False
                elif level == 3:
                    level_three()
                    a = False

            except ValueError:
                logger.warning("This is a ValueError.")
                print("That is invalid input. Please enter either 1, 2, or 3. ")


    def level_one():
        """Level one of the game play, generates random number and has user guess it"""
        my_num = random.randint(1, 10)
        logger.debug("A random number was generated.")
        count = 0

        print("Welcome to level 1! I'm going to pick a number from 1-10, try and guess it!")
        print("Try to have the lowest number of guesses possible. ")

        b = True
        while b:
            a = True
            while a:
                try:
                    guess_ = int(input("Please tell me your guess. "))
                    logger.debug("Valid input would be a integer.")
                    logger.debug("We are saving the user input to a variable named 'guess'")
                    a = False
                except ValueError:
                    print("That's not a number. You must enter your guesses as integers. Try again. ")
                    logger.warning("This is a ValueError Exception.")

            if guess_ < my_num:
                print("That's too low. Try again! ")
                logger.debug("The user's guess should be lower than the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
            elif guess_ > my_num:
                print("That's too high. Try again! ")
                logger.debug("The user's guess should be higher than the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
            else:
                print("That's my number! You won. ")
                logger.debug("The user's guess should be the same as the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
                b = False

        print("Because you guessed " + str(count) + " times, you get " + str(count) + " points. ")
        logger.debug("The game will return the number of guesses based on the 'count' variable.")
        play_again = input("Would you like to play again? ")
        logger.debug("Valid input must be yes or no.")
        a = True
        while a:
            if play_again == "yes":
                logger.debug("If the user wants to play again, the program will move to the game_play() function.")
                game_play()
                a = False
            elif play_again == "no":
                logger.debug("If the user wants to quit, the program should also quit.")
                print("Thank you for playing!")
                quit()
            else:
                logger.warning("This is invalid input.")
                print("Please enter either yes or no.")


    def level_two():
        """Level two of the game play, generates random number and has user guess it"""
        my_num = random.randint(1, 100)
        logger.debug("A random number was generated.")
        count = 0

        print("I'm going to pick a number from 1-100, try and guess it!")
        print("Try to have the lowest number of guesses possible to win. ")

        b = True
        while b:
            a = True
            while a:
                try:
                    guess_ = int(input("Please tell me your guess. "))
                    logger.debug("Valid input would be a integer.")
                    logger.debug("We are saving the user input to a variable named 'guess'")
                    a = False
                except ValueError:
                    print("That's not a number. Try again. ")
                    logger.warning("This is a ValueError Exception.")

            if guess_ < my_num:
                print("That's too low. Try again! ")
                logger.debug("The user's guess should be lower than the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
            elif guess_ > my_num:
                print("That's too high. Try again! ")
                logger.debug("The user's guess should be higher than the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
            else:
                print("That's my number! You won. ")
                logger.debug("The user's guess should be the same as the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
                b = False
        print("Because you guessed " + str(count) + " times, you get " + str(count) + " points. ")
        logger.debug("The game will return the number of guesses based on the 'count' variable.")
        play_again = input("Would you like to play again? ")
        logger.debug("Valid input must be yes or no.")
        a = True
        while a:
            if play_again == "yes":
                logger.debug("If the user wants to play again, the program will move to the game_play() function.")
                game_play()
                a = False
            elif play_again == "no":
                print("Thank you for playing!")
                logger.debug("If the user wants to quit, the program should also quit.")
                quit()
            else:
                logger.warning("This is invalid input.")
                print("Please enter either yes or no. ")


    def level_three():
        """Level three of the game play, generates random number and has user guess it"""
        my_num = random.randint(1, 1000)
        logger.debug("A random number was generated.")
        count = 0

        print("I'm going to pick a number from 1-1000, try and guess it!")
        print("Try to have the lowest number of guesses possible to win.")

        b = True
        while b:
            a = True
            while a:
                try:
                    guess_ = int(input("Please tell me your guess. "))
                    logger.debug("Valid input would be a integer.")
                    logger.debug("We are saving the user input to a variable named 'guess'")
                    a = False
                except ValueError:
                    print("That's not a number. Try again. ")
                    logger.warning("This is a ValueError Exception.")

            if guess_ < my_num:
                print("That's too low. Try again! ")
                logger.debug("The user's guess should be lower than the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
            elif guess_ > my_num:
                print("That's too high. Try again! ")
                logger.debug("The user's guess should be higher than the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
            else:
                print("That's my number! You won. ")
                logger.debug("The user's guess should be the same as the random integer generated.")
                count += 1
                logger.debug("The 'count' variable should be incremented based on how many guesses are received.")
                b = False
        print("Because you guessed " + str(count) + " times, you get " + str(count) + " points. ")
        logger.debug("The game will return the number of guesses based on the 'count' variable.")
        play_again = input("Would you like to play again? ")
        logger.debug("Valid input must be yes or no.")
        a = True
        while a:
            if play_again == "yes":
                logger.debug("If the user wants to play again, the program will move to the game_play() function.")
                game_play()
                a = False
            elif play_again == "no":
                logger.debug("If the user wants to quit, the program should also quit.")
                print("Thank you for playing!")
                quit()
            else:
                logger.warning("This is invalid input.")
                print("Please enter either yes or no. ")


    def main():
        """ Creates parser options for usage, runs the program """
        parser = optparse.OptionParser('-u username ' + '-p password')
        parser.add_option('-u', dest='username', type='string', help="Game username- enter within '' marks")
        parser.add_option('-p', dest='password', type='string', help="Game password- enter within '' marks")
        (options, args) = parser.parse_args()
        u_name = options.username
        p_word = options.password
        # if no username or password is given, print out the usage"
        if u_name is None or p_word is None:
            print(parser.usage)
            exit(0)

        login(u_name, p_word)


    try:
        if __name__ == '__main__':
            main()
    except KeyboardInterrupt:
        print("\nGoodbye!")

except Exception as e:
    print(e)
