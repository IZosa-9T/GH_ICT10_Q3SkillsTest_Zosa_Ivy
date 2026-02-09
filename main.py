from pyscript import display, document, window

def Signup(e):
    document.getElementById('output1').innerHTML = ''

    username = document.getElementById('input1').value
    password = document.getElementById('input2').value

    if len(username) < 7:
        display(f'Invalid input. Username requires at least 7 characters.', target='output1')

    elif len(password) < 10:
        display(f'Invalid input. Password requires at least 10 characters.', target='output1')
        
    elif not password.isalpha():
        if password.isdigit():
            display(f'Password requires letters.', target='output1')
    elif password.isalpha():
        display(f'Password requires numbers.', target='output1')

    else:
        display(f'Password meets requirements.', target='output1')
        display(f'Information meets requirements, account created!', target='output1')