def sdvig(symb, num):
    if symb in '=)(+-*/1234567890 .,?"!\'-'' ':
        return symb
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()

# main
import re

# Считывание предложения
sentence = input()

# Разделение предложения на слова и символы препинания, а также сохранение пробелов как отдельных элементов
s = re.findall(r'\w+|[^\w\s]|\s', sentence)
p = []
for i in range(len(s)):
    for j in range(len(s[i])):
        p.append(sdvig(s[i][j], len(s[i])))
print(''.join(p))
