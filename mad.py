#print('hello Madina')
#print('Hello Arkhat')


# x = 5
# y = 7
# print(x)
# print(x,y)
# print(x+y)
# name = "Madina"
# #print(name)
# surname = "Imangaliyeva"
# print(name,surname) 
# if 6==6:
# 	print(x,y,'matematika')
	# a = "string Madina"
	# b = 77 #integer
	# c = 5.12 #float
	# list1 = [1,2,'ASdsd']
	# dictionary = {
	#  	"a" : "asd",
	#  	"b" : 123
	# }
	# boolean = True #False

# a = '1'
# # a = float(a)
# b = 2.912
# # b = float(b)
# c = 3
# # c = float(c)

# # print(float(a) + float(b) + float(c))
# # print(str(a) + str(b) + str(c))
# print(int(a) + int(round(b)) + int(c))
# print("hello world")


# c = 98.98 # 98
# d = 100 #'100'
# c = int(c)
# d = int(d)
# # print(type(d))
# name = "Madina"
# a = "menya zovut "
# d = " mne "
# c = 24.5
# # a = str(a)
# # name = str(name)
# # d = str(d)
# c = str(c)
# # print(a+name+d+c)
# intro = f" menya zovut {name} mne {c}"
# print(intro)
# a = 6 
# b = 4
# c = 1996
# # print(a + b + c)
# a = '0' + str(6) + "."
# b = "0" + str(4) + "."
# c = str(1996)
# print(a+b+c)
# a = 123
# if a > 200:
# 	print("False")
# elif a == 123:
# 	print("True")
# else:
# 	print("True")


# if a > 10:
# 	print("больше 10ти")
# elif a == 10:
# 	print("ровно 10")
# else:
# 	print("меньше 10ти")


# elif a == 10:
# 	print("ровно 10")
# else:
# 	print("меньше 10ти")

# a = "qShaskl"
# b = 8
# # print(b)
# if b > 5 and  not b < 8:
# 	print("больше 5ти или 8")
# elif b == 5:
# 	print("равно с 5")
# elif b == 7:
# 	print('7777')
# else:
# 	print("ничего из вышеперечисоенного")

a = input('введите а\n')
b = input('введите b\n')
o = input('введите что сделать\n')
a = int(a)
b = int(b)
print(a)
print(b)
if o =='*':
	print(a * b)
elif o =='/':
	print(int(a / b))
elif o =='-':
	print(int(a-b))
elif o =='+' or 'plus' == o:
	print(int(a+b))
else:
	print('выберите правильный оператор')