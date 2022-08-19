# imports
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
            return f'COM{user_input}'
        else:
            print(language["bad_com"])
