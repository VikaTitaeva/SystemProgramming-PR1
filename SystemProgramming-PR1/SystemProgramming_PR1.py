    # первый скрипт для ввода данных в файл
print ("Введите через пробел фамилию, имя, отчество, год рождения")
def isint(i): # функция для проверки, является ли переменная числом
    try:
        int(i)
        return True
    except ValueError:
        return False
while True:
    try:
        file = open('FIO.txt', 'a', encoding='utf8') #открытие файла
        try:
            surname, name, patronymic, yearb = map(str, input().split())
            if surname == '-' and name == '-' and patronymic == '-' and yearb == '-':
                break
            elif isint(yearb) and len(yearb) == 4:# проверка того, что год состоит из 4 цифр
                file.write(str(surname) + ' ' + str(name) + ' ' + str(patronymic) + ' ' + str(yearb) + ' ' + '\n') # запись в файл
            else:
                print('Год состоит из 4-х цифр!')
        except ValueError:
            print('Проверьте правильность введенных данных!')
        finally:
            file.close()
    except:
        print('Файл сломался, система тоже')

        # второй скрипт для чтения файла
print('Фамилия Имя Отчество Год рождения')
try:
    file = open('fio.txt', 'r', encoding='utf8') #открытие файла
    while True:
        list = file.readline()
        if not list:
            break
        print('фамилия ' + ' имя ' + ' отчество ' + ' год рождения ' + '\n')
        print(str(list))
except:
    print('Файл сломался, система тоже')
finally:
    file.close()
