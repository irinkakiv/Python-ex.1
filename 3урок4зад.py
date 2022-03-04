def my_func (x, y):
    try:
        res = x**y
    except TypeError:
        return "Enter a float x and negative y"
    return res

print(my_func(5.2, -2))