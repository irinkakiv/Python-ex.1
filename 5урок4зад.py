rus_dic ={"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text5.txt", "w", encoding= 'utf-8') as new_f:
    with open("text_4.txt", encoding= 'utf-8') as my_f:
        new_f.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_f])