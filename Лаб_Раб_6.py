#№1
#request = int(input('Введите номер кабинета: '))
#
#dictionary = {
#    101: {'key': 1234, 'access': True},
#    102: {'key': 1337, 'access': True},
#    103: {'key': 8943, 'access': True},
#    104: {'key': 5555, 'access': False},
#    None: {'key': None, 'access': False},
#}
#response = dictionary.get(request)
#if not response:
#    response = dictionary[None]
#key = response.get('key')
#access = response.get('access')
#print(key, access)
#
#№2
#from pprint import pprint
#
#my_dict = {'first': 'so easy'}
#
#
#def dict_maker(**kwargs):
#    my_dict.update(**kwargs)
#
#
#dict_maker(a1=1, a2=20, a3=54, a4=13)
#dict_maker(name='Михаил', age=31, weight=70, eyes_color='blue')
#pprint(my_dict)
#
#№3
#input_string = 'HelloWorld'
#result = tuple(input_string)
#print(result)
#print(list(result))
#
#№4
#def personal_info(name, age, company='unnamed'):
#    print(f"Имя: {name} Возраст: {age} Компания: {company}")
#tom = ("Григорий", 22)
#personal_info(*tom)
#bob = ("Георгий", 41, "Yandex")
#personal_info(*bob)
#
#№5
#def tuple_sort(tpl):
#    for elm in tpl:
#        if not isinstance(elm, int):
#            return tpl
#   return tuple(sorted(tpl))
#
#
#if __name__ =='__main__':
#    print(tuple_sort((5, 5, 3, 1, 9)))
#    print(tuple_sort((5, 5, 2.1, '1', 9)))