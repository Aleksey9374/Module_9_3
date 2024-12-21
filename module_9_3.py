'''Необходимо создать 2 генераторных сборки:
В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк
из списков first и second, если их длины не равны. Для перебора строк попарно из двух списков
используйте функцию zip.
В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин
 строк в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip.
  Используйте функции range и len.'''

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs(len(a) - len(b)) for a, b in zip(first, second) if len(a) != len(b))
print(list(first_result))
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))
print(list(second_result))