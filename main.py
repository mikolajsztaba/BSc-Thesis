# main imports
from prettytable import PrettyTable
from serial import Serial
from time import sleep

# imports from other files
from language.json_schema import user_language_choice
from data.decorators import decorator_space
from lib.function_user import configure_user, type_device, user_com, set_hostname, ip_set, ssh_host, ping_all,\
     user_pasword
from data.devices import devices
from data.variables import ip_number, com_speed
from lib.file_handling import delete_files, save_dev_ip
from logger.logging import *
from lib.function_auto import start_tftp, main_choice, del_old_logs, kill_tftp, check_ip_hostname
from lib.ssh_con import ssh_con

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

                    # ip address chosen by the user
                    current_ip = ip_set(lang)

                    # TODO: TUTAJ TEN WYBOR SIECI DO KTOREJ MA NALEZEC NASZ HOST

                    #     tutaj teez wiecej ttrzeba zeby sie wgrywaly konfigi i wczesniej tworzyly itp
                    # try/except block to read the ip number from txt file

                    # check hostname/ip availability
                    if check_ip_hostname(current_ip, hostname, lang):
                        break

                # saving hostname with ip address to txt file
                save_dev_ip(hostname, current_ip)

                # print(user_dev)

            else:
                break
        # SSH CONNECTIONS
        elif user_choice == '2':
            # question about ssh host
            ssh_host = ssh_host(lang)

            # question about login and password
            ssh_credentials = user_pasword(lang)

            # connecting by ssh
            ssh_con(ssh_host, ssh_credentials[0], ssh_credentials[1], lang)

        elif user_choice == '3':
            # start tftp
            start_tftp()

            # function to wait a little be
            sleep(5)

            # kill tftp after config is downloaded
            kill_tftp()

        # function to scan one network by IP addresses:
        elif user_choice == '4':
            # function to print online ip addresses
            ping_all(lang)

        # deleting old console logs
        elif user_choice == '9':
            del_old_logs(lang)

        # deleting all temporary files
        elif user_choice == '0':
            delete_files(lang)

        else:
            break