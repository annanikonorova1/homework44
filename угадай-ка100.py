print("ПОПРОБУЙ УГАДАЙ!")
import random
flag=True
while flag:
 proba=0
 for i in range(1,10):
  a=random.randint(1,1000)
 while proba<10:
    print("Я загадал число от 1 до 100. Попробуйте отгадайте")
    user_num = int(input("Введите число от 1 до 1000:"))
    proba+=1
    if user_num>100:
     print("Вы ввели слишком большое число")
    if user_num<a:
     print ("Ваше число маленькое. Повторите попытку.",{proba+1})
    if user_num>a:
     print("Ваше число большое. Повторите попытку",{proba+1})
    if user_num==a:
     print("Правильно!Ты угадал за", proba,"попыток")
else: 
 print("Не угадал!Я загадал число", format(a))
 flag = True if input('Продолжить?(1/2)')=='1' else False
SystemExit
