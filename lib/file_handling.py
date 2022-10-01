# IMPORTS
import os

from data.decorators import decorator_space, decorator_null

# TXT files handling
def reading_conf_files(file):
    """

    :param file: name of file to be configured
    :return: list with commands to be sent by COM to this device
    """
    with open(f'temp/{file}') as file:
        # getting commands from list
        content_list = file.readlines()
        stripped_list = [s.strip() for s in content_list]
        return stripped_list


# deleting all temporary files created during the script
def delete_files(lang_dict):
    files = os.listdir('temporary')
    for file in files:
        os.remove(f'temporary/{file}')
    print(lang_dict["deleted_files"])
    print(decorator_space)


# function to store device hostname with ip in txt file
def save_dev_ip(hostname, ip):
    try:
        with open("temporary/hostname_ip.txt", "a") as file:
            file.write(f"{hostname} {ip}\n")
    except:
        with open("temporary/hostname_ip.txt", "w") as file:
            file.write(f"{hostname} {ip}\n")


# function to read config provided by the user
def user_config(language):
    # declaring dict with devices
    dict_config = {}
    # printing possible configs
    print(language["user_config_list"])
    # list of possible configs from /user_config folder
    configs_list = os.listdir('user_config')
    # counter to create dict
    counter = 1
    if len(configs_list) > 0:
        # creating dict full of devices
        for x in configs_list:
            dict_config[counter] = x
            counter += 1
        # printing dict pretty
        for key in dict_config:
            print(key, '->', dict_config[key])
    else:
        print(decorator_null)
    print(decorator_space)
    # question about user input
    user_choice = int(input(language["config_number"]))
    # checking if the user has chosen the proper number
    if user_choice in dict_config.keys():
        # reading configuration from the selected file
        with open(f'user_config/{dict_config[user_choice]}') as my_file:
            data = my_file.read()
            # reading commands into list
            commands = data.split("\n")
            # returning commands list
            return commands
    else:
        print(language["wrong_input"])
