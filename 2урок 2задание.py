count = int(input("количество элементов списка"))
my_list = []
i = 0
t = 0
q = 0
while i < count:
    my_list.append(input("следующее значение списка"))
    i += 1
for t in range(0, count-count % 2, 2):
    q = my_list[t]
    my_list[t] = my_list[t+1]
    my_list[t+1] = q
print(my_list)
    
