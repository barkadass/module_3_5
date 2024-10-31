def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return number


result = get_multiplied_digits(40203)
print(result)




# stack = []
# stack.append(1)
# print('Добавили элемент' , stack)
# stack.append(2)
# print('Добавили элемент' , stack)
# stack.append(3)
# print('Добавили элемент' , stack)
# stack.append(4)
# print('Добавили элемент' , stack)
# print(stack)
# stack.pop()
# print('Убрали элемент' , stack)
# stack.pop()
# print('Убрали элемент' , stack)
# stack.pop()
# print('Убрали элемент' , stack)
# stack.pop()
# print('Убрали элемент' , stack)
