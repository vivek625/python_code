import re
class passs:
    def passwd(k):
        while True:
            password = input("Enter a password")
            if len(password) < 8:
                print("make sure your password is at least 8 letter")
            elif re.search('[0-9]',password) is None:
                print("make sure your password has number in it")
            elif re.search('[A-Z]',password) is None:
                print("make sure your password has a capital letter in it ")
            elif re.search('[~!@#$%^&*()_+"<>/?]',password) is None:
                print("make sure your password has a symbol in it")
            else:
                print("your password is fine \n password is stronge")
                break
A = passs()
A.passwd()
