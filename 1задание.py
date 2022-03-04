x = 20
y = 45
print("Переменные x и y - ", x, y)
string1 = input("Введите имя ")
number1 = int(input("Введите первое число "))
string2 = input("Введите второе имя ")
number2 = int(input("Введите второе число "))
print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))

time = int(input("Введите время в секундах "))
hours = time // 3600
min = (time - hours * 3600) // 60
sec = time - (hours * 3600 + min * 60)
print(f"Время в формате чч:мм:сс   {hours} : {min} : {sec}")


n = int(input("Введите число = "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn = %d" % total)


n = int(input("Введите целое положительное число "))
maxi = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > maxi:
        maxi = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", maxi)
        break

        
        profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    worker = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / worker:.2f}")
else:
    print("Фирма работает в убыток")

    
    a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат не менее в км "))
result_days = 1
result_km = 0
while a < b:
        a = a + 0.1 * a
        result_days += 1
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
