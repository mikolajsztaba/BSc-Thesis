# function without user decisions
# imports
import subprocess


# function to start TFTP server
def start_tftp():
    subprocess.Popen([r"tftp_server/tftpd32.exe"])