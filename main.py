# main imports
from prettytable import PrettyTable
from serial import Serial

# imports from other files
from language.json_schema import user_language_choice
from data.decorators import decorator_space
from lib.function_user import configure_user, type_device, user_com
from data.devices import devices
from data.variables import ip_number, com_speed
from lib.file_handling import read_ip_number, save_ip_number, delete_files
from logger.logging import *

# flags
main_flag = True

# choosing language
lang = user_language_choice()

# printing info table about author and Bsc Thesis
table = PrettyTable()
table.title = lang['info']
table.field_names = [lang['author'], lang['script_title'], lang['university'], lang['year']]
table.add_row([lang['name'], lang['title'], lang['college'], lang['date']])
print(decorator_space)
print(table)
print(decorator_space)

# question about downloading config to the devices
conf_flag = configure_user(lang)

# moving into downloading config to the devices
while main_flag:
    if conf_flag:
        # COM CONNECTION
        # choosing COM port number
        #TOOD: maybe add functionality to check possible ports on the device
        com_port = user_com(lang)

        ser = Serial(com_port, com_speed)

        user_dev = type_device(lang, devices)
        #     tutaj teez wiecej ttrzeba zeby sie wgrywaly konfigi i wczesniej tworzyly itp
        # try/except block to read the ip number from txt file
        try:
            current_ip = read_ip_number()
        except:
            current_ip = ip_number

        print(user_dev)
        # saving ip_number for the next device
        save_ip_number(current_ip)

        # reading next ip address
        e = read_ip_number()
        print(e)

        # deleting all temporary files
        # TODO: Move it to the last part of script
        # TODO: Add deleting files from logs after some time etc.
        delete_files(lang)
    else:
        print("NIE KONFIGURUJEMY")
        print("PRZECHODZIMY DO SAMEGO ZARZADZANIA SKRYPTEM")
        test = input("AAA")