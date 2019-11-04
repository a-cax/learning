# -*- coding: utf-8 -*-
# ten kod zapenia poprawne wyświetlanie polskich znaków
# zmienne pomocnicze do petli
c = 0

# warunek rozpoczecia/zakonczenia programu
while c == 0:
    print('Naciśnij dowolny klawisz, aby kontynuować, "Spację", aby zakończyć')
    a = input() #wprowadzenie znaku przez uzytkownika
    c = len(a)  #zmiana wartosci parametru wyjscia z petli
b = ord(a[0])      #odczytanie kodu wprowadzonego znaku

# czesc zasadnicza programu
while b != 32:  #warunek: wprowadzono inny znak niz "Spacja"
    print('Cześć!')
    print('Jak się nazywasz?')
    myName = input()    #wprowadzenie imienia
    print('Miło mi Cię poznać ' + myName)

    print('Proszę podać swoją wagę w kilogramach.')

    # weryfikacja wprowadzenia liczby
    while True:
        myWeight = input()  #wprowadzenie wagi
        try:    #sprawdzenie czy wpisano liczbe
            myWeight = float(myWeight) #rzutowanie na liczbe float
            break
        except:
            print('Proszę podać swoją wagę w kilogramach.')


    print('Dziękuję, proszę podać swój wzrost w metrach.')

    # weryfikacja wprowadzenia liczby
    while True:
        myHeight = input()  #wprowadzenie wzrostu
        try:    #sprawdzenie czy wpisano liczbe
            myHeight = float(myHeight)  #rzutowanie na liczbe float
            break
        except:
            print('Proszę podać swój wzrost w metrach.')

    # obliczenie bmi
    bmi = round(float(myWeight) / float(myHeight ** 2), 2)
    print('Twoje BMI wynosi ' + str(bmi))
    if bmi < 18.5:
        print('Twój wynik to niedowaga.')
    elif 24.9 > bmi > 18.6:
        print('Masz prawidłową wagę.')
    elif 26.9 > bmi > 25:
        print('Masz nadwagę pierwszego stopnia.')
    elif 29.9 > bmi > 27:
        print('Masz nadwagę drugiego stopnia.')
    elif 34.9 > bmi > 30:
        print('Twój wynik to otyłość pierwszego stopnia.')
    elif 39.9 > bmi > 35:
        print('Twój wynik to otyłość drugiego stopnia.')
    elif 49.9 > bmi > 40:
        print('Twój wynik to otyłość trzeciego stopnia, tzw. śmiertelna')
    else:
        print('Twój wynik to otyłość czwartego stopnia, tzw. skrajna.')
    weight_lowest = round(float(18.5 * (myHeight ** 2)), 2)
    weight_heighest = round(float(24.9 * (myHeight ** 2)), 2)

    # opcja dodatkowa
    print('\nCzy chcesz poznać Twoją prawidłową wagę?')
    response = input()
    if response == 'tak':
        print('Twoja największa możliwa waga to ' + str(weight_heighest))
        print('Twoja najniższa możliwa waga to ' + str(weight_lowest))
    c = 0

    # warunek rozpoczecia/zakonczenia programu
    while c == 0:
        print('\nNaciśnij dowolny klawisz, aby kontynuować, "Spację", aby zakończyć')
        a = input()
        c = len(a)
    b = ord(a[0])
    if b == 32:
        break
