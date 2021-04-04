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

# a = input('введите а\n')
# b = input('введите b\n')
# o = input('введите что сделать\n')
# a = int(a)
# b = int(b)
# print(a)
# print(b)
# if o =='*':
# 	print(a * b)
# elif o =='/':
# 	print(int(a / b))
# elif o =='-':
# 	print(int(a-b))
# elif o =='+' or 'plus' == o:
# 	print(int(a+b))
# else:
# 	print('выберите правильный оператор')


# a = input('введите пол\n')
# b = input('введите возраст\n')
# a = str(a)
# b = int(b)
# print(a)
# print(b)
# if (a =='ж' and b >= 18) or (a =='м' and b >= 21):
# 	print('Добро пожаловать')
# elif (a =='ж' and b < 18) or (a =='м' and b < 21):
# 	print('Запрещено')

# a = input('выберите продукт\n')
# b = input('сколько кг\n')
# a = str(a)
# b = int(b)
# if a == "яблоко":
# 	summa = b * 100
# 	print(summa)
# elif a == "груша":
# 	summa = b * 200
# 	print(summa)

# a = input("ваш возраст")
# a = int(a)
# b = input("зарплата")
# if a > 21 and a < 30 and int(b) > 1000000:
# 	print("звони 777568991")
# else:
# 	print("thank you, next")


# a = ["vinograd", 23, 96, 74, 'lozhka']
# print(a[-3])

# d = {
# 	'soz' : 'vinograd',
# 	'cifra' : 23,
# 	"chislo" : 96,
# 	"vozrast" : 74,
# 	'vesh' : 'lozhka'
# 	}
# print(d['vesh'])


# massiv = [1,2,3,1,2,3,2,17,45,7,45,8,'low',2,3,1,3]
# x = 13
# while x < len(massiv):
# 	if massiv[x] == 'low':
# 		print('индекс: ' , x)
# 		break
# 	x = x + 1

# for x in range (0,10):
# 	print('я прграмист')



# for x in range (1,100):
	# print(x)

 # summa = [1, 100]
 # x = 0
 # while x < summa:
 # 		print('индекс: ' , x)
 # 		# bre?"ak
	

# def say_hello(name,age):
# 	print('hello ' + name)
# # 	print(name, age)

# # say_hello('Arkhat', 23)

# import datetime
# n = datetime.datetime.now()
# print(n)

# # def plus(a, b):
# # 	c = a * b
# # 	return c

# jauabi = plus(2, 3)
# print(jauabi)










# # x = 1
# # summa = 0
# # while x <= 5:
# # 	print(x)
# # 	# summa = summa + x
# # 	x = x + 1

# a =['asdz', 'asdas', 'Aza', 'Madina', 'Iza']

import requests
import json
# croco = requests.post('http://example.com/', data={'key': 'value'})
# print(croco.text)

# url = "https://api-football-v1.p.rapidapi.com/v2/predictions/157462"

# headers = {
#     'x-rapidapi-key': "SIGN-UP-FOR-KEY",
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

ploads = {'things':2,'total':25}
r = requests.get('https://httpbin.org/get',params=ploads)
res = r.text
res = json.loads(res)
print(res['args']['total'])

print(res["headers"]['Host'])