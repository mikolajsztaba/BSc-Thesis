# main imports
from prettytable import PrettyTable
from serial import Serial
from time import sleep

# imports from other files
from language.json_schema import user_language_choice
from data.decorators import decorator_space
from lib.function_user import configure_user, type_device, user_com, set_hostname
from data.devices import devices
from data.variables import ip_number, com_speed
from lib.file_handling import read_ip_number, save_ip_number, delete_files, save_dev_ip
from logger.logging import *
from lib.function_auto import start_tftp, main_choice, del_old_logs, kill_tftp, check_ip_hostname

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


# moving into downloading config to the devices
while main_flag:
    print(lang['break_prompt'])
    print(decorator_space)
    while True:
        # printing info about script functionalities with user choice
        user_choice = main_choice(lang)
        print(decorator_space)
        if user_choice == '1':
            # question about downloading config to the devices
            conf_flag = configure_user(lang)
            if conf_flag:

                # COM CONNECTION
                # choosing COM port number
                # TOOD: maybe add functionality to check possible ports on the device
                # com_port = user_com(lang)

                # creating COM number connection
                # ser = Serial(com_port, com_speed)

                # loop to make user choose proper ip address and hostname
                while True:
                    # choosing devices from the list
                    # user_dev = type_device(lang, devices)

                    # choosing hostname as user wants to
                    hostname = set_hostname(lang)

                    # TODO: TUTAJ TEN WYBOR SIECI DO KTOREJ MA NALEZEC NASZ HOST

                    #     tutaj teez wiecej ttrzeba zeby sie wgrywaly konfigi i wczesniej tworzyly itp
                    # try/except block to read the ip number from txt file
                    try:
                        current_ip = read_ip_number()
                    except:
                        current_ip = ip_number

                    # check hostname/ip availability
                    if check_ip_hostname(current_ip, hostname):
                        break

                # saving hostname with ip address to txt file
                save_dev_ip(hostname, current_ip)

                # print(user_dev)
                # saving ip_number for the next device
                save_ip_number(current_ip)

                # reading next ip address
                e = read_ip_number()
                print(e)

            else:
                break
        elif user_choice == '2':
            print("NIE KONFIGURUJEMY")
            print("PRZECHODZIMY DO SAMEGO ZARZADZANIA SKRYPTEM")
            test = input("AAA")

        elif user_choice == '3':
            # start tftp
            start_tftp()

            # function to wait a little be
            sleep(5)

            # kill tftp after config is downloaded
            kill_tftp()

        # deleting old console logs
        elif user_choice == '9':
            del_old_logs(lang)

        # deleting all temporary files
        elif user_choice == '0':
            delete_files(lang)

        else:
            break