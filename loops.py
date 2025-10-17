# for i in range(5):
#     print(i)


# count = 0
# while count <= 5:
#     print(count)
#     count += 1


# number = range(1, 10, 2)
# for num in number:
#     print(num)


import random
height = random.randint(1, 1000)
guess = 0
while height != guess:
    guess = int(input('guess the height: '))
    if guess < height:
        print('number too low')
    elif guess > height:
        print('guess too high')
    else:
        print('congratulation you guessed it')
