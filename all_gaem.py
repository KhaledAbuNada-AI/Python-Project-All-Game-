class Game:  # Craet Class

   #############################################################################
   # Constructor For The Mein Game
    def __init__(self):
        print('Welcome In Full Game .... ^_^ ')
        print('Choose Your Game From Our Collection')
        print('Press[1] : Play Even-Odd Game')
        print('Press[2] : Play Sum_Average_Game')
        print('Press[3] : Play Multipcation_Game')

        self.Choices()

   #############################################################################
    # Available Choices
    def Choices(self): #Craet Choices Method

        while True:
            user_choice = input('Enter Your Choice : ')
            if user_choice == 'end':
                print('Thank you for trusting us and the game experience')
                print('How satisfied are you with the game')
                break

            #############################################################################
            # Handling Exception ( Charachter, 1 2 3)
            try:
                user_choice = int(user_choice)
                if user_choice == 1:
                    self.Even_Odd_Game()
                elif user_choice == 2:
                    self.Sum_Average_Game()
                elif user_choice == 3:
                    self.Multipcation_Game()
                else:
                    print('Please Choose Between 1, 2 or 3')
            except ValueError:
                print('Please Enter A Valid Number')

   #############################################################################
    # Even_Odd_Game Code
    def Even_Odd_Game(self):
        print('Welcome In The Even-Odd Game')
        print('Please Enetr A Number ... And I Will Tell You if it Even Or Odd ')
        print('If You Wanna Close The Game Enetr X ')
        while True:
            number = (input('Enetr Your Num : '))
            if number == 'x':
                print('Closing The Game')
                print('Thanks ...')
                break

            #############################################################################
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

   #############################################################################
    # Sum_Average Game Code
    def Sum_Average_Game(self):
        print('This Game Will Take Several Numbers And Print  Average')
        count = int(input('Hom Many Numbers Would You Like To Sum : '))

        current_count = 0
        Sum = 0

        while current_count < count:
            number = float(input('Enter The Namber : '))
            current_count += 1
            Sum += number

        print('Sum Of All Numbers = ', int(Sum))
        print('Average Of All Numbers = ', int(Sum / count))

   #############################################################################
    # Multipcation Table Game Code
    def Multipcation_Game(self):
        print('Welcom In Multiplication App ')
        print('Please Enter The First Number And The Last Number Of The Multiplication Table')

        start = int(input('Enter The First Number Of The Table : '))
        end = int(input('Enter The Last Number Of The Table : '))

        for i in range(start, end + 1):
            for y in range(1, 13):
                print(i, '*', y, '=', i * y)
            print('<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>')


#############################################################################
# Create Object From The Class
gaem1 = Game()

## By: Khaled Aud Nada
## Email: khaled.nada223@gmail.com
