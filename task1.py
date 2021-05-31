#1.

words = ['разработка', 'сокет', 'декоратор']

for word in words:
    print(f'Содержимое переменной:{word} - тип переменной: {type(word)}')

#те же строки полученные из онлайн конвертера

print("#"*25)

words_utf = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
       b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
       b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']
for word in words_utf:
    print(f'Содержимое переменной:{word} - тип переменной: {type(word)}')


print('#'*30)

########
#2.

list_words = ['class', 'function', 'method']

for word in list_words:
    word= bytes(word, 'utf-8')
    print('тип переменной: {}\n'.format(type(word)))
    print('содержание переменной - {}\n'.format(word))
    print('длинна строки: {}\n'.format(len(word)))

print('#'*30)
##################

#3.

'''
word1 = b'attribute'
word2 = b'класс'
word3= b'функция'
word4 = b'type'   
'''
# на строки записанные на кириллице вылетает исключение
'''  File "/Users/alexpo/task1.py", line 40
    word2 = b'класс'
                        ^
SyntaxError: bytes can only contain ASCII literal characters.
'''

########################
#4.

words4 = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words4:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))
    print('#'*10)

#################################################################

print('#'*30)

#5.

import subprocess


resurs = [['ping', 'yandex.ru'],['ping', 'youtube.com']]

for ping in resurs:

    ping_process = subprocess.Popen(ping, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i<3:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print('#'*30)
            break
########################################################################

#6.

import locale

resurs_string = ['сетевое программирование', 'сокет', 'декоратор']

#Создаем файл
with open('test_file.txt', 'w+') as f:
    for i in resurs_string:
        f.write(i + '\n')

print(f) # печатаем объект файла, что бы узнать его кодировку

file_coding = locale.getpreferredencoding()

# Читаем из файла
with open('test_file.txt', 'r', encoding=file_coding) as f:
    for i in f:
        print(i)
