def is_secure_pass(password):
    is_secure = False


    if len(password) < 8:
        print("At least 8 characters")
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not has_upper:
        print("Add an upper case letter")
    elif not has_lower:
        print("Add a lower case letter")
    elif not has_digit:
        print("Add a number")
    
    if has_upper and has_lower and has_digit:
        is_secure = True

    return is_secure


result = False
while not result:
    insert_pass = input("Insert password: ")
    result = is_secure_pass(insert_pass)

    if not result:
        print("Try again")
    else: 
        print("Password saved")
