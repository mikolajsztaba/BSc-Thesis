# main imports
from prettytable import PrettyTable

# imports from other files
from language.json_schema import user_language_choice
from data.decorators import decorator_space

# choosing language
lang = user_language_choice()

# printing info table about author and Bsc Thesis
table = PrettyTable()
table.title = lang['info']
table.field_names = [lang['author'], lang['script_title'], lang['university'], lang['year']]
table.add_row([lang['name'], lang['title'], lang['college'], lang['date']])
print(decorator_space)
print(table)


