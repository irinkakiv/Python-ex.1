str = input("введите строку,слова через пробел")
my_word = []
num = 1
for i in range(str.count(' ') + 1):
    my_word = str.split()

    if len(my_word[i]) <= 10:
        print(f" {num} {my_word [i]}")
        num += 1
    else:
        print(f" {num} {my_word [i] [0:10]}")
        num += 1