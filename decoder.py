def decode(password):
    new_password = []
    for i in range(0, len(password)):
        new_password.append(str(int(password[i]) - 3))

    new_password = ''.join(new_password)
    return new_password