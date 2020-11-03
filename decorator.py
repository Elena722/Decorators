import sys
import functools
# login_required : checks if the username and password are correct.
# If the login details are correct, move on with the decorated function,
# else print “Username and/or password is incorrect”, then redirect to login_page.
def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(len(data)):
            if data[i]['password'] == _password and data[i]['username'] == _username:
                func(*args, **kwargs)
        else:
            print('Username and / or password is incorrect')
            login_page()
        return
    return wrapper

# admin : checks if the user role is “ADMIN”. If it is, move on with the decorated function,
# else print “Permission denied” then redirect to home_page
def admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(len(data)):
            if data[i]['role'] == 'ADMIN' and data[i]['username'] == _username:
                func(*args, **kwargs)
        else:
            print('Permission denied')
            home_page(_username, _password)
        return
    return wrapper

def login_page():
    global _username
    global _password
    _username = input('Enter username: ')
    _password = input('Enter password: ')
    home_page(_username, _password)

@login_required
def home_page(_username, _password):
    home_responce = input('This is the home page. \n Enter ‘logout’ to exit \n Enter ‘admin’ to go to admin page: ')
    if home_responce == 'admin':
        admin_page(_username, _password)
    elif home_responce == 'logout':
        sys.exit(2)

@login_required
@admin
def admin_page(_username, _password):
    admin_responce = input('This is the admin page \n Enter ‘home’ to go the home page: ')
    if admin_responce == 'home':
        home_page(_username, _password)

if __name__ == '__main__':
    data = [
        {'username': 'Paks', 'password': 'PaKs', 'role': 'ADMIN'},
        {'username': 'Santa', 'password': 'Lalala', 'role': 'USER'},
    ]
    login_page()

