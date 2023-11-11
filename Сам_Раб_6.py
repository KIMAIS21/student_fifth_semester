#№1
#Input = (map(int, input().split()))
#List = list(Input)
#print(List)
#print(tuple(List))
#
#№2
#def main(input_tuple, el):
#    if el in input_tuple:
#        index = input_tuple.index(el)
#        new_tuple = input_tuple[:index] + input_tuple[index+1:]
#        return new_tuple
#    else:
#        return input_tuple
#
#test_tuple_1 = (1, 2, 3)
#test_tuple_2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
#test_tuple_3 = (2, 4, 6, 6, 4, 2)
#
#result_test_tuple_1 = main(test_tuple_1, 1)
#result_test_tuple_2 = main(test_tuple_2, 3)
#result_test_tuple_3 = main(test_tuple_3, 9)
#
#print(result_test_tuple_1, result_test_tuple_2, result_test_tuple_3, sep='\n')
#№3
#import random
#
#
#def count_digits(s):
#    Digit_Count = {}
#    for digit in s:
#        if digit in Digit_Count:
#            Digit_Count[digit] += 1
#        else:
#            Digit_Count[digit] = 1
#    most_common = sorted(Digit_Count.items(), key=lambda x: (-x[1], x[0]))[:3]
#    return {k: v for k, v in most_common}
#
#
#s = ''.join([str(random.randint(0, 9)) for _ in range(15)])
#
#digit_count = count_digits(s)
#
#winner = max(digit_count, key=digit_count.get)
#
#print("Строка случайных цифр:", s)
#print("Количество наиболее встречаемых цифр в порядке возрастания:", digit_count)
#
#
#№4
#def main(input_tuple, digit):
#    if digit in input_tuple:
#        start = input_tuple.index(digit)
#        count = input_tuple.count(digit)
#
#        if count == 1:
#            return input_tuple[start:]
#        elif count >= 2:
#            end = input_tuple.index(digit, start + 1)
#            return input_tuple[start:end + 1]
#        else:
#            return input_tuple
#
#
#test_1 = (1, 2, 4)
#test_2 = (1, 8, 3, 4, 8, 8, 9, 2)
#test_3 = (1, 2, 8, 5, 1, 2, 9)
#
#
#result_1 = main(test_1, 8)
#result_2 = main(test_2, 8)
#result_3 = main(test_3, 8)
#
#print(result_1, result_2, result_3, sep='\n')
#
#№5
#def uniq(lst):
#    unique = []
#    [unique.append(item) for item in reversed(lst) if item not in unique]
#    return tuple(unique)
#
#
#Test_tuple_1 = (1, 2, 3, 3, 2)
#Test_tuple_2 = (2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0)
#Test_tuple_3 = (1, 2, 3, 4, 5, 6, 7)
#
#print(uniq(Test_tuple_1))
#print(uniq(Test_tuple_2))
#print(uniq(Test_tuple_3))
