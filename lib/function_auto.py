# function without user decisions

# imports
import subprocess


# function to start TFTP server
def start_tftp():
    subprocess.Popen([r"tftp_server/tftpd32.exe"])


# function to choose proper functionality of the script
def main_choice(lang):
    print(lang["choosing_number"])
    print(lang["option_1"])
    print(lang["option_2"])
    print(lang['option_3'])
    print(lang['option_0'])
    user_choice = input(lang["type_number"]).title()
    return user_choice
