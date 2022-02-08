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
