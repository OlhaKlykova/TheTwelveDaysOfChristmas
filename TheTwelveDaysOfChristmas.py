# Упр 90. Двенадцать дней Рождества
from functions_ex import converting


def write_song(n):
    print(f'On the {converting(n)} day of Christmas')
    print('my true love sent to me:')
    if n >= 12:
        print('Twelve drummers drumming')
    if n >= 11:
        print('Eleven pipers piping')
    if n >= 10:
        print('Ten lords a-leaping')
    if n >= 9:
        print('Nine ladies dancing')
    if n >= 8:
        print('Eight maids a-milking')
    if n >= 7:
        print('Seven swans a-swimming')
    if n >= 6:
        print('Six geese a-laying')
    if n >= 5:
        print('Five golden rings')
    if n >= 4:
        print('Four calling birds')
    if n >= 3:
        print('Three French hens')
    if n >= 2:
        print('Two turtle doves')
    if n == 1:
        print('A partridge in a pear tree')
        print()
    else:
        print('And a partridge in a pear tree')
        print()


'''Вариант для всего текста'''


def main():
    for i in range(1, 13):
        write_song(i)


'''Вариант для ввода пользователем'''


# def main():
#     a = int(input('введите число в диапазоне 1- 12'))
#     verse = write_song(a)
#     print(verse)

main()
# year = int(input('Введите год:'))
# month = input('Введите месяц:')
# day = int(input('Введите число :'))
# months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',/
# 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']