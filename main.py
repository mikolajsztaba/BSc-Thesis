# main imports
from prettytable import PrettyTable

# imports from other files
from language.json_schema import user_language_choice

# choosing language
lang = user_language_choice()

table = PrettyTable()
x.field_names = ["City name", "", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", lang['title'], 1158259, 600.5])
print(table)
print(lang['title'])

