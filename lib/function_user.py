# imports
import re
import ipaddress
import subprocess
import pyautogui


from data.decorators import decorator_space


# question about downloading config to the devices
def configure_user(language):
    conf_user = input(language['download_config']).title()
    if conf_user == 'Yes' or conf_user == 'Tak':
        return True
    else:
        return False


# question about configuring which type of the devices
def type_device(language, list_devices):
    run_flag = True
    while run_flag:
        print(decorator_space)
        print(language['possible_dev'])
        print(*list_devices, sep=", ")
        print(language["leave_prompt"])
        user_input = input(language['device_conf']).title()
        if user_input in list_devices:
            print("Needs to be done preparing initial config files")
            "TODO: MORE WORK HERE"
            return user_input
        elif user_input == "Break":
            run_flag = False


# question about COM PORT
def user_com(language):
    while True:
        user_input = input(language['com_question']).title()
        if user_input.isdigit():
            print(language["good_com"])
            print(f'COM{user_input}')
            return f'COM{user_input}'
        else:
            print(language["bad_com"])
            print(f'COM{user_input}')


# question about hostname for the device
def set_hostname(language):
    while True:
        user_hostname = input(language['hostname_choice'])
        if re.match("^[A-Za-z][A-Za-z0-9-]*[A-Za-z0-9]$", user_hostname) and len(user_hostname) <= 63:
            print(language['correct_hostname'])
            print(user_hostname)
            return user_hostname
        else:
            print(language['bad_hostname'])
            print(user_hostname)
            print(decorator_space)
            print(language['reference'])
            print(
                'https://www.cisco.com/E-Learning/bulk/public/tac/cim/cib/using_cisco_ios_software/cmdrefs/hostname.htm')
            print(decorator_space)


# function to set ip to the device
def ip_set(language):
    user_ip = input(language['provide_ip'])
    while True:
        try:
            ip = ipaddress.ip_address(user_ip)
            print(language['correct_ip'].format(user_ip))
            print(decorator_space)
            return user_ip
        except ValueError:
            print(language['incorrect_ip'].format(user_ip))
            print(decorator_space)


# function to choose ip address to connect by SSH
def ssh_host(language):
    user_input = input(language['ssh_host'])
    print(decorator_space)
    return user_input


# function to ping all ip addresses in the network
def ping_all(language):
    try:
        # list of available devices
        available_ip = []

        # user input about network to verify
        net_addr = input(language['ping_ip'])

        # Create the network
        ip_net = ipaddress.ip_network(net_addr)

        # Get all hosts on that network
        all_hosts = list(ip_net.hosts())

        # Configure subprocess to hide the console window
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE

        # prompt to inform user that sth is happening
        print(language['progress_work'])

        # For each IP address in the subnet,
        # run the ping command with subprocess.popen interface
        for i in range(len(all_hosts)):
            output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE,
                                      startupinfo=info).communicate()[0]

            # printing dots
            print('.', end='')

            if "Destination host unreachable" in output.decode('utf-8'):
                pass
            elif "Request timed out" in output.decode('utf-8'):
                pass
            else:
                available_ip.append(str(all_hosts[i]))
        print(decorator_space)
        print(language["online_ip"])
        print(*available_ip, sep=", ")
        print(decorator_space)

    except:
        print(language['wrong_input'])
        print(decorator_space)


def user_pasword(language):
    user_login = input(language["user_login"])
    print(decorator_space)
    user_password = pyautogui.password(text=language["user_password"], title='', default='', mask='*')
    print(decorator_space)
    return user_login, user_password
