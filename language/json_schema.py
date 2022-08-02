# main imports


# imports from different files
from language.jsons import language


# functions
def user_language_choice():
    print("WELCOME TO THE SCRIPT")
    while True:
        language_list = language_keys()
        print('Possible languages to choose from:')
        print(*language_list, sep=", ")
        user_language = input("Please choose your native language:\n").title()
        if user_language in language_list:
            language_dict = language[user_language]
            return language_dict


def language_keys():
    language_list = []
    for key in language:
        language_list.append(key)
    return language_list

