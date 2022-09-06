#IMPORTS

from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from time import sleep
from datetime import datetime


# establishing SSH connection
def ssh_con(host, username, password):
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
        # "session_log": f"logs/device_logs/{file}_{host}_{dateStr}.txt"
    }
    with ConnectHandler(**cisco1) as net_connect:
        try:
            # ONE COMMAND WITH TFTP COPY
            ez = net_connect.send_command_timing('ls', cmd_verify=False)
            print(ez)

        # error handling while ssh connection
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)
            print(decorator_1)