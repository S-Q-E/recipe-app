from exceptions import * 

def raise_exception(ex):
    raise ex

def option_input(string):
    result = input(string)
    if not result.isdigit():
        raise UserInputOptionException
    return result


def get_option_input():
    try:
        input_function = option_input
    except NameError:
        input_function = input

    return input_function

def id_input(string):
    id = input(string)
    if id.isdigit():
        return id
    else:
        raise InvalidIdException

def get_id_input():
    try:
        input_function = int(age_input)
    except Exception:
        input_function = input

    return input_function


def confirm_input(string):
    result = input(string)
    if result not in ('y', 'n'):
        raise InvalidInputConfirmException
    return result


def get_confirm_input():
    try:
        input_function = confirm_input
    except NameError:
        input_function = input
    
    return input_function