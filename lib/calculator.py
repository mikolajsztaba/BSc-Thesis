# imports
import ipaddress
from prettytable import PrettyTable

from data.decorators import decorator_space, decorator_null


# function to calculate everything about network
def calculate_network(language):
    # creating pretty table
    net_addr = input(language['ping_ip'])
    ip_net = ipaddress.ip_network(net_addr)
    all_hosts = list(ip_net.hosts())
    print(format(ipaddress.IPv4Address(all_hosts[0])))
    print(len(all_hosts))
    print(all_hosts)
    print(ip_net.network_address)
    print(ip_net.broadcast_address)
