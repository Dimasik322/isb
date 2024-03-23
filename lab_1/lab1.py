from caesar import caesar_encrypt
from frequency import char_frequency
from replace import replace_char, replace_dict
from route_transposition import route_transposition

#tast 1:
#caesar_encrypt('lab_1/task1.txt', 3)
#route_transposition('lab_1/task1.txt', 'keyword')

#task 2:
char_frequency("lab_1/cod1.txt")

dict = { 
    "\n" : 'р', #
    " " : 'р', #
    "a" : 'ч', #
    "c" : 'щ', #
    "2" : ' ', #
    "К" : 'е', #
    "Ь" : 'о', #
    "О" : 'т', #
    ">" : 'с', #
    "Ы" : 'н', #
    "t" : 'и', #
    "r" : 'в', #
    "Л" : 'ж', #
    "," : 'ь', #
    "М" : 'з', #
    "1" : 'я', #
    "Х" : 'ю', #
    "Ч" : 'л', #
    "3" : 'х', #
    "8" : 'ы', #
    "Ф" : 'э', #
    "." : 'ф', #
    "b" : 'ш', #
    "Д" : 'а', #
    "Я" : 'п', #
    "9" : 'ц', #
    "Й" : 'к', #
    "Б" : 'д', #
    "А" : 'г', #
    "0" : 'у', #
    "Е" : 'б', #
    "<" : 'м' #
    #"?" : ',' 
    }

replace_dict("lab_1/cod1.txt", dict) 
