# function without user decisions

# imports
import subprocess
import os
from datetime import datetime
from serial import Serial
from time import sleep

from data.decorators import decorator_space


# function to start TFTP server
def start_tftp():
    subprocess.Popen([r"tftp_server/tftpd32.exe"])


# function to choose proper functionality of the script
def main_choice(lang):
    print(lang["choosing_number"])
    print(lang["option_1"])
    print(lang["option_2"])
    print(lang['option_3'])
    print(lang['option_4'])
    print(lang['option_9'])
    print(lang['option_0'])
    user_choice = input(lang["type_number"]).title()
    return user_choice


# function to delete all old console logs
def del_old_logs(lang):
    exact_time = datetime.date(datetime.now())
    filename_today = f'{exact_time}.txt'
    files = os.listdir('logs/console_logs')
    for file in files:
        if file != filename_today:
            os.remove(f'logs/console_logs/{file}')
    print(lang['deleted_logs'])
    files = os.listdir('logs/ssh_logs')
    for file in files:
        if file != filename_today:
            os.remove(f'logs/ssh_logs/{file}')
    print(decorator_space)


# function to kill tftp server process
def kill_tftp():
    subprocess.call("TASKKILL /F /IM tftpd32.exe", shell=True)


# function to check availability of hostname and ip address
def check_ip_hostname(ip, hostname, language):
    flag = True
    # try and except for the initial first device
    try:
        with open("temporary/hostname_ip.txt", "r") as file:
            data = file.read()
            data_list = data.split("\n")
            print(decorator_space)
            for element in data_list:
                data_split = element.split()
                if hostname in data_split:
                    print(language['duplicate_hostname'])
                    print(language['try_again'])
                    flag = False
                if ip in data_split:
                    print(language['duplicate_ip'])
                    print(language['try_again'])
                    flag = False
            return flag
    except:
        return flag


# function to prepare initial config to download
def prepare_config(language, device):
    if device == 'Cisco Switch':
        with open('configs/cisco-switch') as my_file:
            data = my_file.read()
            commands = data.split("\n")
    elif device == 'Cisco Router':
        with open('configs/cisco-router') as my_file:
            data = my_file.read()
            commands = data.split("\n")
    # returning list full of commands
    return commands


# function to send commands to console
def send_to_console(list_commands, ser_fun: Serial, wait_time: float = 0.2):
        # sending each command independently
        for command in list_commands:
            print(command)
            command_to_send = command + '\r\n'
            # ser_fun.write(command_to_send.encode('utf-8'))
            # sleep(wait_time)
            # string_send = ser_fun.read(ser_fun.inWaiting()).decode('utf-8')
            # printing dots to inform user that script is still working
            # print('.', end='')
            # return string_send
