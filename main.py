# # Fundamental Data Types
# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4)) # 0.5 float

# print(2 ** 2)
# print(5 // 4)
# print(6 % 4)

# # math functions
# print(round(3.1))
# print(round(3.9))

# print(abs(-20))

# # operator precedent
# # ()
# # **
# # * /
# # + -
# print((20 - 3) + 2 ** 2)

# # complex is another data type along with int and float, less common.

# # binary numbers
# print(bin(5))
# print(int('0b101', 2))

# # Variables - stores information in the computer
# # snake_case
# # start with lowercase or underscore
# # letters, numbers, underscores
# # case sensitive
# # don't everwrite keywords

# user_iq = 190
# print(user_iq)

# # constants - good convention is all caps for permanent variable
# PI = 3.14

# # assign multiple variables
# a, b, c = 1, 2, 3

# # augmented assignment operator
# some_value = 5
# print(some_value)
# some_value += 2
# print(some_value)

# # strings
# # ''' will do a multi-line string
# long_string = '''
# WOW
# 0 0
# ---
# '''

# print(long_string)

# # escape sequence
# weather = "\tIt\'s \"kind of\" sunny. \n Hope you have a good day!"
# print(weather)

# # formatted strings
# name = "Johnny"
# age = 55
# print(f"Hi {name}. You are {age} years old.") # called an 'f string'
# print("Hi {0}. You are {1} years old.".format(name, age))
# print("Hi {new_name}. You are {age} years old.".format(new_name="Sally", age=70))

# selfish = '1234567'
# # [start:stop:stepover]
# print(selfish[0:8:2])
# print(selfish[1:])
# print(selfish[:5])
# print(selfish[::1])
# print(selfish[::-1]) # reverse the string

# # immutability - strings in python cannot be changed once created, they can be completely updated
