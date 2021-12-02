import re

def passwdCheck(passwd):
    try:
        passwd=str(passwd)
        if (len(passwd)<6) | (re.search('\d',passwd)==None) | (passwd.lower().find('password')!=-1) | (passwd.isdigit()):
            raise ValueError
    except ValueError:
        return False
    return True    

passwd=input('Input passwd: ')
print(passwdCheck(passwd))