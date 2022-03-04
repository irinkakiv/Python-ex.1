my_list = [5, None, -123, 'True', True, 10.5]
def my_type(i):
    for i in range(len(my_list)):
        print(type(my_list[i]))
    return
my_type(my_list)