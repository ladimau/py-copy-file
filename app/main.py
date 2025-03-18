import os


def copy_file(command : str) -> None:
    if command is None or "cp" not in command:
        print('Command empty or not "cp". Returning...')
        return
    else:
        word_list = command.split(" ")
    try:
        cp_command = word_list[0]
        src_file_name = word_list[1]
        dest_file_name = word_list[2]
    except IndexError:
        print("Sorry, input is not valid!")
        return
    try:
        overflow_word = word_list[3]
    except IndexError:
        print("Nice! Input is correct. Continuing...")
    else:
        print(f"Error... Too many arguments provided,"
              f" first being: {overflow_word}")
    if cp_command != "cp":
        print("Error! No cp command provided. Exiting...")
        return
    if os.path.exists(src_file_name) and src_file_name != dest_file_name:
        with open(src_file_name, "r") as source, \
             open(dest_file_name, "w") as dest:
            for line in source.readlines():
                dest.write(line)
    else:
        print("Error! Invalid input files.")
