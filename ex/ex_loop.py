
'''
    題目：印出九九乘法表
'''
# 印出九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
    print()


'''
    題目：假設有一串數列 nums = [1, 2, 3, 6, 7, 8, 9] 請找到第一個大於 5 的數字後跳出迴圈
'''

nums = [1, 2, 3, 6, 7, 8, 9]
for num in nums:
    if num > 5:
        print(num)
        break

'''
    題目：印出 0-9 的奇數
'''
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
