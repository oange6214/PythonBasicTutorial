
"""
    1. 運算式 expression
    2. 陳述式 statement
    3. 資料型別 data type
    4. 函式 function
    5. 模組 module
    6. 例外 exception
    7. 類別 class
"""


# test
print('hello world v1')

print('c:\some\name')
print(r'c:\some\name')

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
      """)


# Variable
hello_word = 'hello world v2'

print(hello_word)


# If else

if hello_word == 'hello world v2':
    hello_word = 'hello world v3'
else:
    hello_word = 'hello world v3'

print(hello_word)


# Function
class HW:
    def __init__(self):
        pass

    def h_word(self):
        print('hello world, def')

yo = HW()
yo.h_word()
