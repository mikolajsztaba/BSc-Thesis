# question about downloading config to the devices
def configure_user(language):
    conf_user = input(language['download_config']).title()
    if conf_user == 'Yes' or conf_user == 'Tak':
        print("LETS GO KONFIGURACJA")
        return True
    else:
        return False