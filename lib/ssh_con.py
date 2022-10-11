#IMPORTS

from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from time import sleep
from datetime import datetime

from data.decorators import decorator_space


# establishing SSH connection
def ssh_con(host, username, password, language):
    # creating time stamp
    now = datetime.now()
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    dateStr = dateObj.strftime("%d.%m.%Y")
    # configuration of network device
    cisco1 = {
        "device_type": f"autodetect",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # session logger
        "session_log": f"logs/ssh_logs/{host}_{dateStr}.txt"
    }
    try:
        with ConnectHandler(**cisco1) as net_connect:
            try:
                while True:
                    # sending commands to ssh host
                    print(language["leave_prompt"])
                    user_command = input(language["ssh_command"])

                    # leaving ssh connection
                    if user_command.title() == 'Break':
                        print(decorator_space)
                        break
                    else:
                        output = net_connect.send_command_timing(user_command, cmd_verify=False)
                        print(output)

            # error handling while ssh connection
            except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
                print(error)
    except:
        print(language["wrong_input"])
        print(language["try_again"])
        print(decorator_space)


# function to send config by tftp
def ssh_tftp_download(file, host, username, password, server_ip, language):
    # creating time stamp
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")
    dateTimeObj = datetime.now()
    dateObj = dateTimeObj.date()
    dateStr = dateObj.strftime("%d.%m.%Y")
    # configuration of network device
    cisco1 = {
        "device_type": f"autodetect",
        "host": f"{host}",
        "username": f"{username}",
        "password": f'{password}',
        # session logger
        "session_log": f"logs/tftp_logs/{file}_{host}_{dateStr}.txt"
    }
    try:
        with ConnectHandler(**cisco1) as net_connect:
            # TFTP configuration download command
            our_command = f'copy tftp://{server_ip}/{file} startup-config'

            # ONE COMMAND WITH TFTP COPY
            net_connect.send_command_timing(our_command, cmd_verify=False)

            # waiting for tftp downloaded
            sleep(2)

            # sending confirmation of tftp copy
            net_connect.send_command_timing('\n', cmd_verify=False)

            # TODO: think about moving it to the next function
            # command for reloading
            net_connect.send_command_timing('reload', cmd_verify=False)

            # sending confirmation of reloading copy
            net_connect.send_command_timing('\n', cmd_verify=False)

            # waiting to give time to device react
            sleep(2)

    except:
        print(language["wrong_input"])
        print(language["try_again"])
        print(decorator_space)
