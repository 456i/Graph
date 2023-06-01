numbers = input('Введите два числа: ').split()
numbers = list(map(int, numbers))
print(numbers)
number_1 = numbers[0]
number_2 = numbers[1]
ten = 10
power = 1

global new_str
new_str = f'{number_1} {number_2} = '


def make_new_str(num_1, num_2):
    global new_str
    buffer_str = ''
    buffer_int = num_1

    for num in str(buffer_int):
        if num_2 > int(num):
            index = str(num_1).index(num)
            print(index)
            count = len(str(num_1)[index:])
            print(count)
            for i in range(count):
                buffer_str += str(num_2)
                print(buffer_str, '1 con')
            buffer_int = num_1 - int(buffer_str)
            new_str += buffer_str + ' + '
            print(new_str)
            make_new_str(buffer_int, num_2)

        elif num_2 == int(num):
            buffer_str += str(num_2)
            print(buffer_str, '2 con')

    new_str += buffer_str + ' + '
    print(new_str)


make_new_str(number_1, number_2)
