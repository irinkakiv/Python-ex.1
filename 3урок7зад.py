def int_func (word):
    latin_char= 'zxzcvbnmasdfghjklqwertyuiop'
    return word.title() if not set(word).difference(latin_char) else False

words = input('введите строку из слов разделенных пробелом:').split()
for w in words:
    result=int_func(w)
    if result:
        print(result, ' ')
