
from pyscript import display, document, window

def confirm_validity(e):
    document.getElementById('validity_message').innerHTML = ' '
    username = document.getElementById('viewer_username').value
    password = document.getElementById('viewer_password').value

    if not len(username) >= 7:
        if len(username) == 6:
            display(f'error 1, username lacks 1 more character', target='validity_message')
        elif len(username) == 5:
            display(f'error 1, username lacks 2 more characters', target='validity_message')
        elif len(username) == 4:
            display(f'error 1, username lacks 3 more characters', target='validity_message')
        elif len(username) == 3:
            display(f'error 1, username lacks 4 more characters', target='validity_message')
        elif len(username) == 2:
            display(f'error 1, username lacks 5 more characters', target='validity_message')
        elif len(username) == 1:
            display(f'error 1, username lacks 6 more characters', target='validity_message')
        elif len(username) == 0:
            display(f'error 1, username lacks 7 more characters', target='validity_message')

    elif not len(password) >= 10:
        if len(password) == 9:
            display(f'error 2, password lacks 1 more character', target='validity_message')
        elif len(password) == 8:
            display(f'error 2, password lacks 2 more characters', target='validity_message')
        elif len(password) == 7:
            display(f'error 2, password lacks 3 more characters', target='validity_message')
        elif len(password) == 6:
            display(f'error 2, password lacks 4 more characters', target='validity_message')
        elif len(password) == 5:
            display(f'error 2, password lacks 5 more characters', target='validity_message')
        elif len(password) == 4:
            display(f'error 2, password lacks 6 more characters', target='validity_message')
        elif len(password) == 3:
            display(f'error 2, password lacks 7 more characters', target='validity_message')
        elif len(password) == 2:
            display(f'error 2, password lacks 8 more characters', target='validity_message')
        elif len(password) == 1:
            display(f'error 2, password lacks 9 more characters', target='validity_message')
        elif len(password) == 0:
            display(f'error 2, password lacks 10 more characters', target='validity_message')

    elif not password.isalpha():
        if password.isdigit():
            display(f'error 3, password requires at least 1 letter', target='validity_message')
        else:
            display(f'account successfully created', target='validity_message')

    elif password.isalpha():
        display(f'error 3, password requires at least 1 digit', target='validity_message')
