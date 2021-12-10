import re

def passwdCheck(passwd):
    '''Check password and return True, if it correct
    and False, if incorrect
    '''
    try:
        passwd=str(passwd)
        if ((len(passwd) < 6) or 
        (re.search('\d',passwd) == None) or 
        (passwd.lower().find('password') != -1) or
        (passwd.isdigit())):
            raise ValueError
    except ValueError:
        return False
    return True    

passwd = input('Input passwd: ')
print(passwdCheck(passwd))