num = int(input('Введие число от 1 до 100000:')) 
if num%num == 0 and num%1 == 0 and num%2 == 1:
    print('Ваше число простое')
if num%num == 0 and num%1 == 0 and num%2 == 0:
    print('Ваше число составное')
elif num<100000 and num<0:
    print ('Вы ввели недопустимое значение')
    
