def reading_conf_files(file):
    """

    :param file: name of file to be configured
    :return: list with commands to be sent by COM to this device
    """
    with open(f'temp/{file}') as file:
        # getting commands from list
        content_list = file.readlines()
        stripped_list = [s.strip() for s in content_list]
        return stripped_list


def read_ip_number():
    with open('temporary/ip_number.txt', 'r') as file:
        new_ip = file.read()
        ip_number = int(new_ip)
        return ip_number


def save_ip_number(ip_number):
    with open('temporary/ip_number.txt', 'w') as file:
        file.write(str(ip_number+1))
