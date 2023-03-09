def password_decoder(password):
    password = list(password)
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] -= 3
        password[i] = str(password[i])

    password = ''.join(password)
    return password


print(password_decoder(input('Please enter your password: ')))
