# IMPORTS
import os

from data.decorators import decorator_space

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


# reading ip number from txt file
def read_ip_number():
    with open('temporary/ip_number.txt', 'r') as file:
        new_ip = file.read()
        ip_number = int(new_ip)
        return ip_number


# saving ip number to txt file incremented by 1
def save_ip_number(ip_number):
    with open('temporary/ip_number.txt', 'w') as file:
        file.write(str(ip_number+1))


# deleting all temporary files created during the script
def delete_files(lang_dict):
    files = os.listdir('temporary')
    for file in files:
        os.remove(f'temporary/{file}')
    print(lang_dict["deleted_files"])
    print(decorator_space)
