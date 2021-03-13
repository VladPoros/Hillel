from string import ascii_uppercase
s = '0123456789' + ascii_uppercase
first_val = int(input('Number: '))
second_val = int (input('System conversation from 2 to 36 : '))

def conv (number, system):
    if 2 <= system <= 36:
        if number<system:
            return s[number]
        while number > 0:
            return conv(number//system,system) + s[number%system]
    else:
        raise ValueError('Second value is not correct system={}'.format(system))

result = conv(first_val, second_val)
print('Result: ' + str(result))

def sec_conv (number, system):
    lst = []
    while number > 0:
        lst.insert(0, s[number%system])
        number = number // system
    output = ''.join([str(i) for i in lst])
    return output

result2 = sec_conv(first_val, second_val)
print('Result: ' + str(result2))