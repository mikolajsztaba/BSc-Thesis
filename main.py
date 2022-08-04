# main imports
from prettytable import PrettyTable

# imports from other files
from language.json_schema import user_language_choice
from data.decorators import decorator_space
from lib.function_user import configure_user

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

if conf_flag:
    print("KONFIGURUJEMY")
else:
    print("NIE KONFIGURUJEMY")
    print("PRZECHODZIMY DO SAMEGO ZARZADZANIA SKRYPTEM")