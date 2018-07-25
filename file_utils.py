# Taylor Cella
# File Input/Output Assignment


def file_io(f_name, f_mode, *f_text):
    """This function opens a file and determines how to handle it"""
    name = f_name
    mode = f_mode
    text = f_text

    # Error handling for if a file is requested that doesn't exist
    try:
        # reads the content of a file that already exists
        if mode == "r":
            with open(name, 'r') as f:
                contents = f.read()
                print(contents)

        # Creates a new file or re-writes a file that already exists
        elif mode == "w":
            with open(name, 'w') as f:
                if text:
                    # Prints each line of text provided individually
                    for lines in text:
                        f.writelines(lines + "\n")
                else:
                    # Lets users know if they didn't specify any text to write
                    print("You didn't enter any text to write to the file.")

        # Creates a new file or appends a file that already exists
        elif mode == "a":
            with open(name, 'a') as f:
                if text:
                    # Prints each line of text provided individually
                    for lines in text:
                        f.writelines(lines + "\n")
                else:
                    # Lets users know if they didn't specify any text to write
                    print("You didn't enter any text to write to the file.")

        # reads and writes a new file or one that already exists
        elif mode == "r+":
            with open(name, 'r+') as f:
                if text:
                    # Puts each line of text in the file and prints it to the console
                    for lines in text:
                        f.write(lines + "\n")
                    contents = f.read()
                    print(contents)
                else:
                    # If text is not included, then only prints the file to the console
                    contents = f.read()
                    print(contents)

        # Only lets users use r, w, or r+ as a valid file mode
        else:
            print("I'm sorry, that is an invalid mode. Please try again.")

    # used for the read mode
    except FileNotFoundError:
        print("I'm sorry, that file does not exist.")
