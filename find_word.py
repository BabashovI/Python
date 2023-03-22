import random
from terminaltables import SingleTable
# ===================================================
words = ['baku', 'moscow', 'tokyo', 'london', 'ankara']
# words=['bakubaku']
# random.shuffle(words)

wrd = random.choice(words)
# print(wrd[-1:],'\n')


def lst():
    find_word = [' _' for _ in wrd]
    table_instance = SingleTable(find_word)
    table_instance.outer_border = True
    table_instance.inner_heading_row_border = True
    table_instance.inner_column_border = True
    table_instance.inner_row_border = True
    print(table_instance.table)
    return find_word


def find(k):
    # find_word=lst()
    while k > 1:
        x = input('enter alf: ')
        if x in wrd and x != '':
            for i in range(len(wrd)):
                if x == wrd[i]:
                    find_word[i] = x
            print(find_word)
            if wrd == find_word:
                print('You win!!!')
                return find_word
        else:
            print(''.join(find_word))
            k -= 1
            print('You left {} try'.format(k-1))


def main():
    lst()
    find(10)


main()
