print('Welcome In The Even-Odd Game')
print('Please Enetr A Number ... And I Will Tell You if it Even Or Odd ')
print('If You Wanna Close The Game Enetr X ')
while True:
    number = (input('Enetr Your Num : '))
    if number == 'x':
        print('Closing The Game')
        print('Thanks ...')
        break
# even number % 2 = 0
    try:
        number = int(number)
        if number % 2 == 0:
            print('Even Number')
            print('-----------------------------------------')

        else:
            print('Add Number')
            print('-----------------------------------------')
    except ValueError:
        print('Please Enetr A Valid Number')