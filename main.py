# main imports
from prettytable import PrettyTable

# imports from other files
from language.json_schema import user_language_choice
from data.decorators import decorator_space
from lib.function_user import configure_user, type_device
from data.devices import devices
from data.variables import ip_number
from lib.file_handling import read_ip_number, save_ip_number

# flags
main_flag = True

# choosing language
lang = user_language_choice()

# printing info table about author and Bsc Thesis
table = PrettyTable()
table.title = lang['info']
table.field_names = [lang['author'], lang['script_title'], lang['university'], lang['year']]
table.add_row([lang['name'], lang['title'], lang['college'], lang['date']])
print(decorator_space)
print(table)
print(decorator_space)

# question about downloading config to the devices
conf_flag = configure_user(lang)

# moving into downloading config to the devices
while main_flag:
    if conf_flag:
        conf_flag = type_device(lang, devices)
        #     tutaj teez wiecej ttrzeba zeby sie wgrywaly konfigi i wczesniej tworzyly itp
        try:
            current_ip = read_ip_number()
        except:
            current_ip = ip_number

        # saving ip_number for the next device
        save_ip_number(current_ip)

        e = read_ip_number()

    else:
        print("NIE KONFIGURUJEMY")
        print("PRZECHODZIMY DO SAMEGO ZARZADZANIA SKRYPTEM")
        test = input("AAA")
