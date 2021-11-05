#lab 5 exercise-2
#name - İbrahim Enes Köse
#id -   2200356055

def check(word):
    if "@" in word and "." in word:
        return True
    return False

mail = input()
if check(mail):
    print("It's a valid e-mail")
else:
    print("It's not a valid e-mail")
