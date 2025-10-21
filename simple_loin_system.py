# while True:
#     password = input('input login password (or exit to stop):')
#     if password.lower() == 'exit':
#         break

#     if len(password) < 9:
#         print('password is too short')
#     elif password == 'python123':
#         print('access granted')
#         break
#     else:
#         print('wrong password try again')




while True:
    password = input('Input login password (or exit to stop): ').strip()
    if password.lower() == 'exit':
        break
    if not password:
        print('Password cannot be empty')
    elif password != 'python123':
        print('Wrong password, try again')
    elif password == 'python123':
        print('Access granted')
        break