# imports
import os

from data.decorators import decorator_space, decorator_null


# function to inform user to put config in folder
def inform_user_config(language):
    print(language["inform_config"])
    print(decorator_space)
    while True:
        user_input = input(language["ready_user"]).lower()
        if user_input == 'yes':
            return True
        elif user_input == 'break':
            break
        else:
            pass
