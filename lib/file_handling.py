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
