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