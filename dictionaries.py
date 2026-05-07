student = {'name': 'Joel', 'Age': '23', 'topics': ['javascript', 'python']}

print(f'hello',student['name'], 'you are', student['Age'], 'years old')

student['Phone'] =  input()
print(student)

for key, value in student.items():
    print(key, value)


details = {}
details['name'] = input('input your name:')
details['password'] = input('input your password:')

if len(details['password']) < 8:
    print('password might not be safe!')
else:
    print('password is safe')
print(f'welcome, your name is', details['name'], 'and your pasword is', details['password'])

# print(len(details['password']))