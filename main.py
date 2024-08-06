from itertools import product
DICT = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def number_input():
    try:
        digits = input('Vvedite chislo is cifr "23456789", 9999 - max\n')
        if digits == '':
            return ''
        if one_and_zero_check(digits):
            return number_input()
    except ValueError:
        print('Vvedi norm chislo!')
        return number_input()
    return digits


def one_and_zero_check(digits):
    if int(digits) > 9999:
        print('Vvedi chislo <9999')
        return True
    for i in str(digits):
        if i == '1' or i == '0':
            print('Vvedite chislo bez 1 i 0')
            return True
    return False


# def list_maker():
#     digit = number_input()
#     if len(digit) == 0:
#         return []
#     answer_list = ['']
#     len_list = 1
#     for i in digit:
#         len_list *= len(DICT[i])
#     print(len_list)
#     answer_list = answer_list * len_list
#
#     return answer_list
# print(list_maker())

def maker():
    digit = number_input()
    args = []
    for i in digit:
        args.append(DICT[i])
    combo_list = list(product(*args))
    answer = []
    for i in combo_list:
        answer.append(''.join(i))
    return answer


print(maker())
