a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат не менее в км "))
result_days = 1
result_km = 0
while a < b:
        a = a + 0.1 * a
        result_days += 1
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
