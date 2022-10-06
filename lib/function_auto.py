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
    try:
        subprocess.Popen([r"tftp_server/tftpd32.exe"])
    except:
        pass


# function to choose proper functionality of the script
def main_choice(lang):
    print(lang["choosing_number"])
    print(lang["option_1"])
    print(lang["option_2"])
    print(lang['option_3'])
    print(lang['option_4'])
    print(lang['option_5'])
    print(lang['option_6'])
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
def kill_tftp(language):
    print(language['tftp_kill'])
    try:
        # os.system("taskkill /f /im tftpd32.exe")
        subprocess.run("taskkill /f /im tftpd32.exe", stdout=subprocess.DEVNULL)
    except:
        pass


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


# creating and reading conf files
def create_conf_switch(content_list, hostname, port_num, netmask, ip_add):
    for x in content_list:
        # changing hostname
        if x == 'hostname xxx':
            our_index = content_list.index(x)
            content_list[our_index] = f'hostname {hostname}'
        # changing interface for whole range
        if x == 'interface GigabitEthernet1/1':
            int_index = content_list.index(x)
            content_list[int_index] = f'interface range GigabitEthernet1/1-{str(port_num)}'
        # changing ip address
        if x == ' ip address x.x.x.x y.y.y.y':
            ip_index = content_list.index(x)
            content_list[ip_index] = f' ip address {str(ip_add)} {str(netmask)}'
    with open(f'temporary/switch-{hostname}-{str(ip_add)}', 'w') as file:
        for row in content_list:
            file.write(str(row) + '\n')
    with open(f'temporary/switch-{hostname}-{str(ip_add)}', 'r') as my_file:
        data = my_file.read()
        ready_commands = data.split("\n")
    # returning ready commands to be sent to the device
    return ready_commands


# function to prepare initial config to download
def prepare_config(language, device, ip, netmask, hostname):
    if device == 'Cisco Switch':
        with open('configs/cisco-switch') as my_file:
            data = my_file.read()
            commands = data.split("\n")
            print(commands)
            # returning list full of commands
            ready_conf = create_conf_switch(commands, hostname, 2000, netmask, ip)
            return ready_conf
    elif device == 'Cisco Router':
        with open('configs/cisco-router') as my_file:
            data = my_file.read()
            commands = data.split("\n")


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


# function to check if the port numer 69 is free for tftp server
def check_tftp():
    output_netstat = str(subprocess.check_output("netstat -na | findstr /R ^UDP", shell=True)).strip()
    check_string = 'UDP    0.0.0.0:69'
    # checking if server works, use return in for example while loop
    if check_string in output_netstat:
        return False
    else:
        return True
