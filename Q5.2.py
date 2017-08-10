def print_binary(num_str):
    array = num_str.split('.')
    num1, num2 = int(array[0]), float('0.' + array[1])  # 3, 0.3

    str1 = ''
    while num1 > 0:
        s = num1 & 1  # find value of the last bit
        str1 = str(s) + str1
        num1 >>= 1

    str2 = ''
    while num2 > 0:
        num2 *= 2 # move 1 bit to right, cannot use bitwise
        if num2 >= 1: # find value of the last bit
            str2 += '1'
            num2 -= 1
        else:
            str2 += '0'

    return str1 + '.' + str2

if __name__ == '__main__':
    print print_binary('16.2')