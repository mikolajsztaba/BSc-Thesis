# main imports
from prettytable import PrettyTable
from serial import Serial
from time import sleep

# imports from other files
from language.json_schema import user_language_choice
from data.decorators import decorator_space
from lib.function_user import configure_user, type_device, user_com, set_hostname, ip_set, ssh_host, ping_all, \
    user_pasword, print_logs, print_temp, network_mask_set
from data.devices import devices
from data.variables import ip_number, com_speed
from lib.file_handling import delete_files, save_dev_ip, user_config, tftp_configs
from logger.logging import *
from lib.function_auto import start_tftp, main_choice, del_old_logs, kill_tftp, check_ip_hostname, prepare_config, \
    send_to_console, check_tftp, go_conf_mode, checking_ports, gen_crypto_keys
from lib.ssh_con import ssh_con, ssh_tftp_download
from lib.input_functions import inform_user_config
from lib.calculator import calculate_network
from lib.booting import checking_booting

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
                    user_dev = type_device(lang, devices)

                    # choosing hostname as user wants to
                    hostname = set_hostname(lang)

                    # ip address chosen by the user
                    current_ip = ip_set(lang)

                    # netmask chosen by the user
                    current_netmask = network_mask_set(lang)

                    # check hostname/ip availability
                    if check_ip_hostname(current_ip, hostname, lang):
                        break

                # checking if the device is booted
                # boot_flag = checking_booting(ser)

                # counting number of ports in the devices
                print(lang['count_ports'])
                print(decorator_space)
                try:
                    giga_port = checking_ports(ser)
                except:
                    giga_port = 10

                boot_flag = True

                # if the device is booted going well
                if boot_flag:
                    # TODO NEEDS TO BE UPGRADED
                    # preparing initial config for the device
                    commands = prepare_config(lang, user_dev, current_ip, current_netmask, hostname, giga_port)
                    print(commands)

                    # going to conf mode
                    try:
                        go_conf_mode(ser)
                    except:
                        pass

                    # trying to generate cryptokeys on the device
                    try:
                        gen_crypto_keys(ser)
                    except:
                        pass


                    # sending commands to the device
                    try:
                        send_to_console(commands)
                    except Exception as error:
                        print(lang["error_info"])
                        print(error)
                        print(decorator_space)

                    # saving hostname with ip address to txt file
                    save_dev_ip(hostname, current_ip)
                else:
                    print(lang["error_info"])

                # closing ser com connection
                try:
                    ser.close()
                except:
                    pass
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
            # checking tftp port is taken
            tftp_flag = check_tftp()

            # trying to start tftp server
            if tftp_flag:
                # print instruction to put config in proper folder
                print(lang['tftp_user_conf'])
                print(decorator_space)

                # printing tftp configs
                server_flag, user_file_tftp = tftp_configs(lang)

                if server_flag:
                    # start tftp
                    start_tftp()

                    # printing prompt about choosing proper configuration in tftp server window
                    print(lang["tftp_option"])
                    print(decorator_space)

                    # ip address chosen by the user (SERVER ADDRESS)
                    print(lang['hostname_IP'])
                    current_server_ip = ip_set(lang)

                    # ip address chosen by the user (HOST NETWORK DEVICE ADDRESS)
                    print(lang["network_device_IP"])
                    current_device_ip = ip_set(lang)

                    # question about username and password
                    username, password = user_pasword(lang)

                    # downloading configs by tftp
                    ssh_tftp_download(user_file_tftp, current_device_ip, username, password, current_server_ip, lang)

                    # TODO: DELETE IT
                    # function to wait a little
                    sleep(1)

                    # kill tftp after config is downloaded
                    kill_tftp(lang)
            else:
                print(lang["tftp_port"])

            print(decorator_space)

        # function to scan one network by IP addresses:
        elif user_choice == '4':
            # function to print online ip addresses
            ping_all(lang)

        # function to download config created by the user to the device
        elif user_choice == '5':
            # function to inform user
            config_flag = inform_user_config(lang)
            # choosing config
            if config_flag:
                user_config_file = user_config(lang)
                print(user_config_file)

                # NEEDS TO BE COMMENTED
                # creating com ports
                # com_port = user_com(lang)

                # creating COM number connection
                # ser = Serial(com_port, com_speed)

                # sending commands to the device
                try:
                    send_to_console(user_config_file)
                except Exception as error:
                    print(lang["error_info"])
                    print(error)
                    print(decorator_space)

        # function to calculate hosts in the network
        elif user_choice == '6':
            print("FUNCTION TO CALCULATE")
            calculate_network(lang)

        # deleting old console logs
        elif user_choice == '9':
            # question about deleting logs and printing it
            del_flag = print_logs(lang)
            if del_flag:
                del_old_logs(lang)

        # deleting all temporary files
        elif user_choice == '0':
            del_flag = print_temp(lang)
            if del_flag:
                delete_files(lang)

        else:
            break
