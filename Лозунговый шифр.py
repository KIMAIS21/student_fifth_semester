# Функция шифрования вводных данных
def crypt(inp, alfa, alfa2):
    res = ''
    for i in range(len(inp)):
        res += alfa[alfa2.index(inp[i])]
    return res

# Функция расшифровки зашифрованных данных
def decrypt(inp, alfa, alfa2):
    res = ''
    for i in range(len(inp)):
        res += alfa2[alfa.index(inp[i])]
    return res


if __name__ == "__main__":

    # Ввод данных
    codeword = input('Введите кодовое слово: ')
    inp = input('Введите текст для шифрования: ')
    codeword = codeword.lower()
    inp = inp.lower()

    # Массивы под алфавиты
    alfa =[]
    alfa2 = []

    # Вывод ошибки
    try:
        pass
    except SyntaxError as e:
        print('Ошибка: ', e)

    # Проверка на язык (ру)
    if ord(inp[0]) in range(ord('а'), ord('я')):

        # Проверка на правильный ввод данных для кодового слова
        for i in range(len(codeword)):
            if ord(codeword[i]) not in range(ord('а'), ord('я')):
                if codeword[i] == ' ':
                    pass
                else:
                    raise SyntaxError('Неверно задано ключевое слово')

        # Проверка на правильный ввод данных для текста для шифрования
        for i in range(len(inp)):
            if ord(inp[i]) not in range(ord('а'), ord('я')):
                if inp[i] == ' ':
                    pass
                else:
                    raise SyntaxError('Неверно задано ключевое слово')

        # Добавление элементов массива через таблицу ASCII (Русский)
        for i in range(ord('а'), ord('я') + 1):
            alfa.append(chr(i))
            alfa2.append(chr(i))
        for i in range(len(codeword)):
            alfa.pop(alfa.index(codeword[i]))
            alfa.insert(i, codeword[i])

    # Проверка на язык (ENG)
    elif ord(inp[0]) in range(ord('a'), ord('z')):

        # Проверка на правильный ввод данных для кодового слова
        for i in range(len(codeword)):
            if ord(codeword[i]) not in range(ord('a'), ord('z')):
                if codeword[i] == ' ':
                    pass
                else:
                    raise SyntaxError('Неверно задано кодовое слово')

        # Проверка на правильный ввод данных для текста для шифрования
        for i in range(len(inp)):
            if ord(inp[i]) not in range(ord('a'), ord('z')):
                if inp[i] == ' ':
                    pass
                else:
                    raise SyntaxError('Неверно задано кодовое слово')

        # Добавление элементов массива через таблицу ASCII (Анлийский)
        for i in range(ord('a'), ord('z') + 1):
            alfa.append(chr(i))
            alfa2.append(chr(i))
        for i in range(len(codeword)):
            alfa.pop(alfa.index(codeword[i]))
            alfa.insert(i, codeword[i])

    # Добавление в конец алфавита пробел для шифрования больших текстов
    alfa.append(' ')
    alfa2.append(' ')

    # Вызов функций
    a = crypt(inp, alfa, alfa2)
    print(a)
    print(decrypt(a, alfa, alfa2))
