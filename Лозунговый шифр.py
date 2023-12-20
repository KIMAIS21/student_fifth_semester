def crypt_ru(codeword, inp):
    alfaR = []
    alfaR2 = []
    res = ''
    for i in range(ord('а'), ord('я') + 1):
        alfaR.append(chr(i))
        alfaR2.append(chr(i))
    for i in range(len(codeword)):
        alfaR.pop(alfaR.index(codeword[i]))
        alfaR.insert(i, codeword[i])
    for i in range(len(inp)):
        res += alfaR[alfaR2.index(inp[i])]
    return res


def decrypt_ru(codeword, inp):
    alfaR = []
    alfaR2 = []
    res = ''
    for i in range(ord('а'), ord('я') + 1):
        alfaR.append(chr(i))
        alfaR2.append(chr(i))
    for i in range(len(codeword)):
        alfaR.pop(alfaR.index(codeword[i]))
        alfaR.insert(i, codeword[i])
    for i in range(len(inp)):
        res += alfaR2[alfaR.index(inp[i])]
    return res


def crypt_EN(codeword, inp):
    alfaEN = []
    alfaEN2 = []
    res = ''
    for i in range(ord('a'), ord('z') + 1):
        alfaEN.append(chr(i))
        alfaEN2.append(chr(i))
    for i in range(len(codeword)):
        alfaEN.pop(alfaEN.index(codeword[i]))
        alfaEN.insert(i, codeword[i])
    for i in range(len(inp)):
        res += alfaEN[alfaEN2.index(inp[i])]
    return res


def decrypt_EN(codeword, inp):
    alfaEN = []
    alfaEN2 = []
    res = ''
    for i in range(ord('a'), ord('z') + 1):
        alfaEN.append(chr(i))
        alfaEN2.append(chr(i))
    for i in range(len(codeword)):
        alfaEN.pop(alfaEN.index(codeword[i]))
        alfaEN.insert(i, codeword[i])
    for i in range(len(inp)):
        res += alfaEN2[alfaEN.index(inp[i])]
    return res


if __name__ == "__main__":
    codeword = input('Введите кодовое слово: ')
    inp = input('Введите текст для шифрования: ')
    codeword = codeword.lower()
    inp = inp.lower()

    try:
        pass
    except SyntaxError as e:
        print('Ошибка: ', e)

    if ord(inp[0]) in range(ord('а'), ord('я')):
        for i in range(len(codeword)):
            if ord(codeword[i]) not in range(ord('а'), ord('я')):
                raise SyntaxError('Неверно задано ключевое слово')
        for i in range(len(inp)):
            if ord(inp[i]) not in range(ord('а'), ord('я')):
                raise SyntaxError('Неверно задано ключевое слово')
        a = crypt_ru(codeword, inp)
        print(a)
        print(decrypt_ru(codeword, a))

    if ord(inp[0]) in range(ord('a'), ord('z')):
        for i in range(len(codeword)):
            if ord(codeword[i]) not in range(ord('a'), ord('z')):
                raise SyntaxError('Неверно задано ключевое слово')
        for i in range(len(inp)):
            if ord(inp[i]) not in range(ord('a'), ord('z')):
                raise SyntaxError('Неверно задано ключевое слово')
        a = crypt_EN(codeword, inp)
        print(a)
        print(decrypt_EN(codeword, a))
