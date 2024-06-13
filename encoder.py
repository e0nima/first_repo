def custom_input():
    power_alph = 26 if input('Please, choose the alphabet: EN or RU\n') == 'EN' else 32
    bin_track = 2 if input('Please, choose encode or decode text?\n') == 'encode' else 1
    key_word = input('Please, insert the key_word\n')
    key_num = int(input('Please, insert the key_num\n'))
    text = input('Please, insert ur text\n')
    return power_alph, bin_track, key_word, key_num, text

def sdvig(track, key_num, key_word, i_sim, non_alph_counter):
    return  ((-1) ** track) * key_num * (ord(key_word[(i_sim - non_alph_counter)%len(key_word)]) - ord('a') + 1)

def encode_symbol(sym, i_sim, non_alph_counter, alph_power, track, key_word, key_num):
    if not sym.isalpha():
        return sym, non_alph_counter + 1    # non_alph & count that
    elif ord('A') <= ord(sym) <= ord('Z'):   # upper EN
        return chr((ord(sym) + sdvig(track, key_num, key_word, i_sim, non_alph_counter) - ord('A'))%alph_power + ord('A')), non_alph_counter
    elif ord('a') <= ord(sym) <= ord('z'):   # lower EN
        return chr((ord(sym) + sdvig(track, key_num, key_word, i_sim, non_alph_counter) - ord('a'))%alph_power + ord('a')), non_alph_counter
    elif ord('А') <= ord(sym) <= ord('Я'):   # upper RU
        return chr((ord(sym) + sdvig(track, key_num, key_word, i_sim, non_alph_counter) - ord('А'))%alph_power + ord('А')), non_alph_counter
    elif ord('а') <= ord(sym) <= ord('я'):   # lower RU
        return chr((ord(sym) + sdvig(track, key_num, key_word, i_sim, non_alph_counter) - ord('а'))%alph_power + ord('а')), non_alph_counter
            

def text_code(text, track, alph_power, key_word, key_num):
    res_text = ['' for i in range(len(text))]
    non_alph_counter = 0
    for i in range(len(text)):
            res_text[i], non_alph_counter = encode_symbol(text[i], i, non_alph_counter, alph_power, track, key_word, key_num)
    return res_text
        



# main

power_alph, bin_track, key_word, key_num, text = custom_input()
res_text = text_code(text, bin_track, power_alph, key_word, key_num)
print('This text:')
print(''.join(text))
print('Turns into:')
print(''.join(res_text))


