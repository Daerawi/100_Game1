while True:

    #print("~~~~~ THE 100 GAME - CODED BY Taqi Mayoof  ~~~~~")
    #print ("ID : 20170417")
    #print ("G-15")
    print('<<<< MENU >>>>')
    print('1 - Start 100 game')
    print('2 - Quit game')
    choice = int(input('What are you going to do? Input the number representing your choice.'))
    if choice == 1:
        print('alright lets start the game....')
    elif choice == 2:
        print('Thanks for passing by ,See you later.')
        break  # In order to stop the program and quit.
    
    while True:
        print("player 1, What's your name:")
        Player1 = input()
        print('What about you....player 2:')
        Player2 = input()
        print('So , ' + Player1 + ' and ' + Player2 + ',  welcome to 100Game hope you enjoy')
        print('you both players will start from 0 .')
        print('and alternatively add a number from 1 -> 10 to the sum .')
        print('The player who reaches 100 wins ')
        print("Once again hope you enjoy the game.....")
        totalNumber = 0
        while True:
            while totalNumber < 100:
                x = input( Player1  + ', give me a number between 1 and 10.') 
                x = int(x)
                if ( x  > 10 or x  < 0):
                    print ("error number try again")
                    break  #i havent got any other ideas to prevent it from exceed the range number.



                    
                totalNumber += x 
                print("Got it, " + Player1 + "! Below is the total right now:")
                print(totalNumber)
                if (totalNumber>=100) :
                    print(Player1 + "you are the winner")
                
                
            
                y = input(Player2 + ', give me a number between 1 and 10.')
                y = int(y)
                
                if (y > 10 or y  < 0):#i havent got any other ideas to prevent it from exceed the range number.
                    print ("error number try again")
                    break

                totalNumber += y 
                print("Got it, " + Player2 + "! Below is the total right now:")
                print(totalNumber)
                if (totalNumber>=100) :
                    print(Player2 + "you are the winner") #cant make him go back to menu....
            break 
