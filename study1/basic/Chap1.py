import math

print(8 // 2 * (2 + 2))

print(math.sqrt(math.pow(550, 2) + math.pow(600, 2)))

# 2-1
# num = int(input())
#
# result = num
#
# while num > 0:
#     num-=1
#     print(result)

# 2-2

# num = int(input())
#
# for i in range (1,num+1) :
#     print(i, (i*i))

# 2-3
# num = 100
# for val in range(1, 11):
#     num = num * (3 / 5)
#     print(val, round(num, 4))
#
# # 2-4
# number = 358
#
# rem = rev = 0
# while number >= 1:
#     rem = number % 10
#     rev = rev * 10 + rem
#     number = number // 10
#
# print(rev)

# 2-3-3

input_base = input()
num_base = list(map(int, input_base.split()))

temp_base = input()
temp = list(map(int, temp_base.split()))

for val in temp:
    if num_base[0] <= val <= num_base[1]:
        print("Nothing")
    elif val == -999 : break
    else:
        print("Alert")
        break
