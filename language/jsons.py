# dict structure with prompts
language = {"En": {
                    "title": "Design of a tool for automatic configuration of network devices and network control.",
                    "script_title": "Title of BSc Thesis",
                    "college": "AGH",
                    "university": "University",
                    "author": "Author",
                    "name": "Mikołaj Sztaba",
                    "year": "Academic year",
                    "date": "2022-2023",
                    "info": "Main info about the script",
                    "download_config": "If you are sure that your computer has COM port type 'yes':\n",
                    "device_conf": "Which device do you want to configure?\n",
                    "possible_dev": "Possible devices to choose from:",
                    "leave_prompt": "If you want to leave this part of the script type 'Break'.",
                    "deleted_files": "All temporary files were successfully deleted.",
                    "com_question": "Which COM port would you like to use? Type only number: \n",
                    "good_com": "Proper input of COM port: ",
                    "bad_com": "Wrong input of COM port. Try again!",
                    "break_prompt": "If you want to leave any parts of script just type 'break'!",
                    "choosing_number": "Choose option provided by the script by typing the number:",
                    "option_1": "1 -> Downloading configs by COM port to the devices.",
                    "option_2": "2 -> Script managing by LAN network.",
                    "option_3": "3 -> Downloading config by TFTP Server.",
                    "option_4": "4 -> Discover working devices in the network.",
                    "option_5": "5 -> Downloading config provided by the user to the device.",
                    "option_6": "6 -> Network calculator.",
                    "option_9": "9 -> Delete old script logs.",
                    "option_0": "0 -> Delete all temporary script files.",
                    "type_number": "Type your number:\n",
                    "deleted_logs": "Old logs were successfully deleted.",
                    "hostname_choice": "Please provide your hostname for this device: \n",
                    "correct_hostname": "Your hostname was provided correctly:",
                    "bad_hostname": "Your hostname is not supported: ",
                    "reference": "Reference:",
                    "duplicate_ip": "Your IP address is overlapped with the previous ones.",
                    "duplicate_hostname": "Your hostname is overlapped with the previous ones.",
                    "try_again": "Try again please...",
                    "provide_ip": "Please provide your ip like 192.168.1.1: \n",
                    "correct_ip": "IP address {} is valid.",
                    "incorrect_ip": "IP address {} is not valid.",
                    "ssh_host": "Which IP address you want to connect?\n",
                    "ping_ip": "Enter a network address in CIDR format(ex. 192.168.1.0/24):\n",
                    "wrong_input": "Something went wrong... Check your input if it is correct!",
                    "progress_work": "Work in progress:",
                    "online_ip": "Online devices in the network:",
                    "user_login": "Please provide your login:\n",
                    "user_password": "Please provide your password:\n",
                    "ssh_command": "Please type in your command: \n",
                    "ssh_logs": "Possible ssh logs:",
                    "console_logs": "Possible console logs:",
                    "logs_question": "If you want to delete logs type 'yes', if not type anything else: \n",
                    "bad_device": "Device is not handled, try again...",
                    "lab_device": "Device in lab: \nRouter -> Cisco 4231, \nSwitch -> Catalyst 3650",
                    "error_info": "Something went wrong:",
                    "temporary_files": "Temporary files created during the script:",
                    "temp_files_question": "If you want to delete temporary files type 'yes', if not type anything else: \n",
                    "user_config_list": "Possible configs in '/user_config' folder:",
                    "config_number": "Please provide number of chosen config:\n",
                    "inform_config": "Please put your config file in 'user_config' folder!",
                    "ready_user": "If you are ready type 'yes', if you want to leave type 'break':\n",
                    "mask_input": "Please provide network mask as a number for example 24:\n",


                  },
            "Pl": {
                    "title": "Stworzenie narzędzia do automatyzacji konfiguracji urządzeń sieciowych oraz sterowania działaniem sieci.",
                    "script_title": "Tytuł pracy inżynierskiej",
                    "college": "AGH",
                    "university": "Uniwersytet",
                    "author": "Autor",
                    "name": "Mikołaj Sztaba",
                    "year": "Rok akademicki",
                    "date": "2022-2023",
                    "info": "Główne informacje o skrypcie",
                    "download_config": "Jeżeli twój komputer ma COM port wpisz 'Tak':\n",
                    "device_conf": "Które urządzenie sieciowe chcesz skonfigurować?\n",
                    "possible_dev": "Możliwe urządzenia do skonfigurowania:",
                    "leave_prompt": "Jeżeli chcesz opuścić tą część skryptu wpisz 'Break'.",
                    "deleted_files": "Wszystkie tymczasowe pliki zostały usunięte.",
                    "com_question": "Którego numeru portu COM chcesz użyć? Wpisz tylko liczbę: \n",
                    "good_com": "Poprawny numer COM portu: ",
                    "bad_com": "Zły numer COM portu. Spróbuj ponownie!",
                    "break_prompt": "Jeżeli chcesz opuscic jakas czesc skryptu wpisz 'break'!",
                    "choosing_number": "Wpisz odpowiednią cyfrę, aby wybrać funkcjonalność:",
                    "option_1": "1 -> Pobieranie configów przez COM port na urządzenie.",
                    "option_2": "2 -> Zarządzanie skryptem przez sieć LAN.",
                    "option_3": "3 -> Pobieranie configów na urządzenia poprzez serwer TFTP.",
                    "option_4": "4 -> Odkrycie wszystkich dostępnych adresów IP.",
                    "option_5": "5 -> Pobieranie configu podanego przez użytkownika na urządzenie.",
                    "option_6": "6 -> Kalkulator sieciowy.",
                    "option_9": "9 -> Usunięcie starych logów z działania skryptu...",
                    "option_0": "0 -> Usunięcie wszystkich tymczasowych plikow konfiguracyjnych.",
                    "type_number": "Wpisz swój numer:\n",
                    "deleted_logs": "Logi konsolowe zostały poprawnie usunięte.",
                    "hostname_choice": "Wpisz nazwę dla tego konkretnego urządzenia: \n",
                    "correct_hostname": "Twój hostname został wybrany poprawnie:",
                    "bad_hostname": "Twój hostname nie jest poprawny:",
                    "reference": "Referencje: ",
                    "duplicate_ip": "Twój adres IP powtarza się juz z wcześniej użytymi.",
                    "duplicate_hostname": "Twój hostname powtarza się już z wcześniej użytymi.",
                    "try_again": "Spróbuj ponownie...",
                    "provide_ip": "Proszę wpisz swój adres IP tak jak np. 192.168.1.1: \n",
                    "correct_ip": "IP adres {} jest poprawny.",
                    "incorrect_ip": "IP adres {} nie jest poprawny. Spróbuj ponownie...",
                    "ssh_host": "Do którego adresu IP chcesz się połączyć?\n",
                    "ping_ip": "Wpisz adres sieci w formacie CIDR np. 192.168.1.0/24):\n",
                    "wrong_input": "Coś poszło nie tak, sprawdź czy twoje dane sa poprawne.",
                    "progress_work": "Praca w toku:",
                    "online_ip": "Osiągalne adresy ip w sieci:",
                    "user_login": "Wpisz swój login:\n",
                    "user_password": "Wpisz swoje hasło:\n",
                    "ssh_command": "Wpisz swoją komendę: \n",
                    "ssh_logs": "Zapisane logi ssh:",
                    "console_logs": "Zapisane logi z konsoli:",
                    "logs_question": "Jeżeli chcesz usunąć logi wpisz 'yes', jeżeli nie wpisz cokolwiek innego: \n",
                    "bad_device": "To urządzenie nie jest obslugiwane, spróbuj ponownie...",
                    "lab_device": "Urządzenia w labie: \nRouter -> Cisco 4231, \nSwitch -> Catalyst 3650",
                    "error_info": "Coś poszło nie tak:",
                    "temporary_files": "Pliki tymczasowe stworzone podczas działania skryptu:",
                    "temp_files_question": "Jeżeli chcesz usunąć pliki tymczasowe wpisz 'yes', jeżeli nie wpisz cokolwiek innego: \n",
                    "user_config_list": "Dostępne konfiguracje w folderze '/user_config':",
                    "config_number": "Wpisz numer wybranej konifguracji:\n",
                    "inform_config": "Proszę umieścić swój config w folderze 'user_config'!",
                    "ready_user": "Jeśli jesteś gotowy wpisz 'yes', jeśli chcesz wyjść wpisz 'break':\n",
                    "mask_input": "Wpisz maskę sieciową jako numer np. 24:\n",

            }
}
