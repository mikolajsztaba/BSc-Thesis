# function without user decisions

# imports
import subprocess
import os
from datetime import datetime

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

