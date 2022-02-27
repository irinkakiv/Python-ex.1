
my_f = open('text_1.txt', 'w', encoding='utf-8')

line = " "
while line:
    line = input("Введите строку или пустую для завершения: ")
    my_f.write(f"{line}\n") if line != '' else my_f.close()
