# main imports
from prettytable import PrettyTable

# imports from other files
from language.json_schema import user_language_choice

# choosing language
lang = user_language_choice()

table = PrettyTable()
table.field_names = [lang['author'], lang['script_title'], lang['university'], lang['year']]
table.add_row([lang['name'], lang['title'], lang['college'], lang['date']])
print(table)

