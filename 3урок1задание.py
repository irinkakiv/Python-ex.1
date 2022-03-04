def div(*args):

    try:
        arg1 = int(input("Input delimoe"))
        arg2 = int(input("Input delitel"))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong delitel! nelzia delit na 0"
    return res
print(f'result  {div()}')
