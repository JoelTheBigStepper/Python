# for i in range(5):
#     print(i)
#     if i == 3:
#         break


# for i in range(11):
#     if i == 7:
#         print('it is', i,'am wake up')


# for i in range(1, 13):
#     for j in range(1, 13):
#         print(i , j, end="\t")
#     print()  # Move to new line after each row


# for i in range(10):
#     print('hello world', i)
#     if i == 2:
#         continue
#     elif i == 5:
#         print('hello humans', i +1)
#         continue


# height = 1.745
# guess = 0
# while height != guess:
#     guess = float(input('input height:'))
#     if guess > height:
#         print('greater than height')
#     elif guess < height:
#         print('lesser than height')
#     else:
#         print('correct height')

# count = 0
#     count += 1


# number = range(1, 10, 2)
# for num in number:
#     print(num)


# import random
# height = random.randint(1, 1000)
# guess = 0
# while height != guess:
#     guess = int(input('guess the height: '))
#     if guess < height:
#         print('number too low')
#     elif guess > height:
#         print('guess too high')
#     else:
#         print('congratulation you guessed it')



# Nested Loops and Loop Control Statements
# for num in range(2, 10):
#     for i in range(2, num): 
#         if num % i == 0:
#             print(f"{num} is not prime")
#             break
#     else:
#         print(f"{num} is prime")


# for i in range(4):
#     for j in range(4):
#         print(f"i: {i}, j: {j}")

for i in range(10, -1, -1):
    print(i)
print("Liftoff!")
