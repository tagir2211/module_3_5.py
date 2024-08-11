def get_multiplied_digits(number):
    number_str = str(number)
    if len(number_str) == 1:
        if number_str != '0':
            return int(number_str)
        else:
            return 1
    else:
        first = int(number_str[0])
        if first == 0:
            return 1
        else:
            return first * get_multiplied_digits(int(number_str[1:]))

print(get_multiplied_digits(40203))
