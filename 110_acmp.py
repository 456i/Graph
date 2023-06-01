numbers = input('Введите два числа: ').split()
numbers = list(map(int, numbers))
print(numbers)
number_1 = numbers[0]
number_2 = numbers[1]
result = f'{number_1} {number_2} = '


def generate_beautiful_numbers(num_1, num_2, delta=1):
    global result
    buffer_str = ''
    buffer_int = num_1
    power = 1
    out = False
    for digit in str(buffer_int):
        if num_2 < int(digit) and not out:
            for i in range(len(str(num_1)[str(num_1).index(digit):])):
                buffer_str += str(num_2)
            buffer_int = num_1 - int(buffer_str)
            result += buffer_str + ' + '
            generate_beautiful_numbers(buffer_int, num_2)
            out = True

        elif num_2 == int(digit) and not out:
            buffer_str += str(num_2)
            if num_2 - num_1 == 0:
                result += buffer_str

        elif num_2 > int(digit) and not out:
            delta += 1
            power = 10 ^ delta
            generate_beautiful_numbers(buffer_int, num_2/power, delta)
            out = True


generate_beautiful_numbers(number_1, number_2, 1)
print(result)

