birthdate = input("Enter your birthdate in format DD/MM/YYYY: ").split("/")
cake = "   |:H:a:p:p:y:|\n __|___________|__\n|^^^^^^^^^^^^^^^^^|\n|:B:i:r:t:h:d:a:y:|\n|                 |\n~~~~~~~~~~~~~~~~~~~"
year = int(birthdate[-1])
leap_year_flag = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year_flag = True
    else:
        leap_year_flag = True
candles = int(birthdate[-1][-1])
cake = " "*4 + '_'*int((11-candles)/2) + 'i'*candles + '_'*int((11-candles)/2) + " "*4 + '\n' + cake
if candles % 2 == 0:
    cake = cake[:9]+'_'+cake[9:]
print(cake)
if leap_year_flag:
    print(cake)