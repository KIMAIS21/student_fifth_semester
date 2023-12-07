Задание 5
class CustomException(Exception): #Класс принимающие сообщения и выводящий сообщения об ошибке
    def __init__(self, error):
        self.error = error
        super().__init__(self.error)

cifri = ['1', '2',  '3', '4', '5', '6', '7', '8', '9', '0'] #Массив цифр для проверки строки
def stoka(text): #Функция разбития строки на массив символов
    razbitie_stroki = []
    for i in range(len(text)): #Цикл перебора символов
        symbol = text[i]
        if symbol in cifri:
            raise CustomException('Обнаружена цифра') 
        elif symbol == ' ':
            pass
        else:
            razbitie_stroki.append(symbol)
    return razbitie_stroki

def Poryadok(stroka): #Функция для выстроения в алфавитный порядок символов
    for i in range(len(stroka)): #Проверка на повторяющиеся символы
        if stroka.count(stroka[i]) > 1:
            raise CustomException('Символы повторяются')
    for i in range(len(stroka)): #Цикл перестоновки символов
        for j in range(i, len(stroka)):
            if ord(stroka[i]) < ord(stroka[j]):
                stroka[i], stroka[j] = stroka[j], stroka[i]
    stroka.reverse()
    print(stroka)

#Тесты
try: 
    test1 = stoka('время шло')
    Poryadok(test1)

except CustomException as e:
    print(f'Произошло исключение: {e.error}')

try:
    test2 = stoka('быть 1')
    Poryadok(test2)

except CustomException as e:
    print(f'Произошло исключение: {e.error}')

try:
    test3 = stoka('где ты был')
    Poryadok((test3))

except CustomException as e:
    print(f'Произошло исключение: {e.error}')
