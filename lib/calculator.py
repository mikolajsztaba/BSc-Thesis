# imports
import ipaddress
from prettytable import PrettyTable

from data.decorators import decorator_space, decorator_null


# function to calculate everything about network
def calculate_network(language):
    # try and except block to be error reliable
    try:
        # creating pretty table
        table = PrettyTable()
        # add table title
        table.title = "NETWORK CALCULATOR REPORT"
        # add first info raw
        table.field_names = ['Variable', 'Value']
        # question about getting network in CIDR format
        net_addr = input(language['ping_ip'])
        # creating network
        ip_net = ipaddress.ip_network(net_addr, strict=False)
        # getting all hosts
        all_hosts = list(ip_net.hosts())
        # calculating wildcard
        wildcard = str(
            ipaddress.IPv4Address(int(ipaddress.IPv4Address._make_netmask(f'{ip_net.netmask}')[0]) ^ (2 ** 32 - 1)))
        # checking if the address is private
        if ip_net.is_private:
            is_private = 'Private'
        else:
            is_private = 'Public'
        # converting netmask into binary
        netmask_split = str(ip_net.netmask).split('.')
        temp_list = []
        for x in netmask_split:
            binary_octet = format(int(x), '08b')
            temp_list.append(binary_octet)
        netmask_string = '.'.join(temp_list)

        # class declaration
        classes = {
            "A": ipaddress.IPv4Network(("10.0.0.0", "255.0.0.0")),
            "B": ipaddress.IPv4Network(("172.16.0.0", "255.240.0.0")),
            "C": ipaddress.IPv4Network(("192.168.0.0", "255.255.0.0")),
        }
        ip = ipaddress.ip_address(net_addr.split('/')[0])
        for class_name, network in classes.items():
            if ip in network:
                ip_class = class_name
                break
        else:
            ip_class = 'Unknown'

        # putting variables into table
        table.add_row(['IP Address:', net_addr.split('/')[0]])
        table.add_row(['Network Address:', ip_net.network_address])
        table.add_row(['Usable Host IP Range:',
                       f'{format(ipaddress.IPv4Address(all_hosts[0]))} - {format(ipaddress.IPv4Address(all_hosts[-1]))}'])
        table.add_row(['Broadcast Address:', ip_net.broadcast_address])
        table.add_row(['Total Number of Hosts:', len(all_hosts) + 2])
        table.add_row(['Number of Usable Hosts:', len(all_hosts)])
        table.add_row(['Subnet Mask:', ip_net.netmask])
        table.add_row(['Wildcard Mask:', wildcard])
        table.add_row(['Binary Subnet Mask:', netmask_string])
        table.add_row(['IP Class:', ip_class])
        table.add_row(['CIDR NOTATION:',  f'/{net_addr.split("/")[1]}'])
        table.add_row(['IP Type:', is_private])

        # printing table with variables and values
        print(table)
    except:
        print(language['wrong_input'])
        print(decorator_space)
