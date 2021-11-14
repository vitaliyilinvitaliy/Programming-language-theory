from dka_class import DKA

# Формат заполнения конфиг файла (.csv)
#
# 1 строка
#       1 ячейка - количество состояний (int)
#       2 ячейка - номер начального состояние (int)
#       3 ячейка - перечень конечный состояний через пробелы (int) 
# 2 строка
#       1 ячейка - алфавит языка через пробелы
#
# в последующих строках задается матрица переходов 
# размер матрицы = количество состояний * количество состояний
# в ячейках через пробел пишутся символы по которым можем перейти 
# в состояне, индекс которого равен индексу столбца
# если переход отсутствует, то пишем символ -

def main():
    test_dka = DKA("conf_dka.csv")
    test_dka.display_dka() 
    
    input_chain = ''

    print('\nEnter \'exit\' to terminate the program!\n')

    while 1:
        print('Input chain: ', end='')
        input_chain = str(input())
        
        if input_chain == 'exit':
            break

        test_dka.check_chain(input_chain)

if __name__ == '__main__':
    main()
