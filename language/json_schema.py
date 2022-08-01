# main imports
import json

# imports from different files
from language.jsons import prompts_pl, prompts_en

# structures
available_languages = ['en', 'pl']


# functions
def user_language_choice():
    while True:
        print('Possible languages to choose from:')
        print(*available_languages, sep=", ")
        user_input = input("Please provide your native language:\n").lower()
        if user_input in available_languages:
            if user_input == 'en':
                language = json.loads(prompts_en)
            if user_input == 'pl':
                language = json.loads(prompts_pl)
            return language
