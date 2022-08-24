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