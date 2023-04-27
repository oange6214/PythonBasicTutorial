'''
    題目：由使用者輸入數字，檢查數字是否為正數
'''

num = int(input("請輸入一個數字: "))
if num > 0:
    print("這個數字是正數")
else:
    print("這個數字不是正數")

'''
    題目：由使用者輸入年份，檢查年份是否為閏年
'''

year = int(input("請輸入一個年份: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("這是一個閏年")
else:
    print("這不是一個閏年")


'''
    題目：由使用者輸入字串，判斷一個字串是否為迴文
'''

string = input("請輸入一個字串: ")
if string == string[::-1]:
    print("這個字串是迴文")
else:
    print("這個字串不是迴文")



'''
    題目：由使用者輸入數字，檢查一個數字是否為質數
'''

num = int(input("請輸入一個數字: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("這個數字不是質數")
            break
    else:
        print("這個數字是質數")
else:
    print("這個數字不是質數")