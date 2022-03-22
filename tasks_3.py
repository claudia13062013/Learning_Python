
# EXERCISE 16 :

import time
import random
def easy(num, examples):
    number = random.randint(0, 4)
    password = examples[number]
    if len(password) == num:
        return str(password)
    elif len(password) < num:
        for i in range(len(password), num):
            password = password + "i"
        return str(password)
    elif len(password) > num:
        password = "12345"
        for i in range(len(password), num):
            password += "i"
        return str(password)
def change_password(num, y, examples):
    password = []
    upper_l = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    lower_l = ["q","w",'e',"r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    digit = ["1","2","3","4","5","6","7","8","9","0"]
    symb = [".", "_", "@", "-", "!", "$"]
    if y == "y" or y == "Y":
        return easy(num, examples)
    else:
        for i in range(0, num):
            letter = random.randint(1, 4)
            if letter == 1:
                password.append(upper_l[random.randint(0, len(upper_l)-1)])
            elif letter == 2:
                password.append(lower_l[random.randint(0, len(lower_l)-1)])
            elif letter == 3:
                password.append(digit[random.randint(0, len(digit)-1)])
            elif letter == 4:
                password.append(symb[random.randint(0, len(symb)-1)])
        password = "".join(password)
        return str(password)
if __name__=="__main__":
    while True:
        examples = []
        print("")
        print("~~~~~~~~~~~~~~~~~~~~PASSWORD GENERATOR~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("Your Name:")
        name = input("")
        examples.append(name + "12345")
        examples.append(name + "ABCDE")
        examples.append(name.upper() + "12345")
        examples.append(name + "00001")
        examples.append(name + "09876")
        print("How long your password should be (minimum 6 letters)?")
        while 1:
            try:
                num = int(input(""))
                break
            except ValueError:
                print("NO your password should have minimum 6 letters! How long your password should be ?")

        if num < 6:
            while num < 6:
                print("NO your password should have minimum 6 letters! How long your password should be ?")
                while 1:
                    try:
                        num = int(input(""))
                        break
                    except ValueError:
                        print("NO your password should have minimum 6 letters! How long your password should be ?")
        print("")
        print("If you want easy password enter 'Y' ")
        y = input("")

        new = change_password(num, y, examples)
        print("Generating password...")
        time.sleep(3)
        print("~~~~~~~~~~")
        time.sleep(3)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(3)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(2)
        print("Your Password : " + new)
        print("Do you want new password ? Enter 'Y' if yes ")
        n = input("")
        if n == "y" or n == "Y":
            continue
        else:
            break


