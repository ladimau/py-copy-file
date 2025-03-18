import os


def copy_file(command : str) -> None:
    if command is None or "cp" not in command:
        print('Command empty or not "cp". Returning...')
        return
    else:
        command_provided = command.split(" ")
    try:
        cp_command = command_provided[0]
        src_file_name = command_provided[1]
        dest_file_name = command_provided[2]
    except IndexError:
        print("Sorry, input is not valid!")
        return
    try:
        overflow_word = command_provided[3]
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
