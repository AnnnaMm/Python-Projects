import random

class Player():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def rozdacha_kart(self):
        self.N = 5
        #self.player_cards1 = [random.randint(1, 9) for self.i in range(self.N)]
        #self.player_cards2 = [random.randint(1, 9) for self.i in range(self.N)]
        self.player_cards1 = [1,2,3,4,5]
        self.player_cards2 = [1,2,3,4,5]

    def vyvid(self):
        print('Гравець № 1 : ',self.player1,'| Карти гравця : ' , self.player_cards1 )
        print('Гравець № 2 : ',self.player2,'| Карти гравця : ' , self.player_cards2 )

#class Game(Player):

    def start(self):
        self.stil = []
        print()
        print('---------------------------START---------------------------')
        print()
        print('Гравець 1 :',self.player1, self.player_cards1, '||', 'СТІЛ :', self.stil, '||','Гравець 2 :', self.player2, self.player_cards2)

        for i in range(self.N):
            print()
            print('*********************************************************')
            print()
            self.stil.insert(0, self.player_cards1.pop()) 
            self.stil.insert(0, self.player_cards2.pop())
            if self.player_cards2[-1] == self.stil[0]:
              #  del self.stil[0]
                self.player_cards1.insert(0,self.player_cards2[-1])
            if self.player_cards1[-1] == self.stil[0]:
               # del self.stil[0]
                self.player_cards2.insert(0,self.player_cards1[-1])
            

            if all([ i % 2 != 0 for i in self.player_cards1 ]) or all([ i % 2 != 0 for i in self.player_cards2]):
        
                print('Гравець 1 :',self.player_cards1,'Гравець 2 :',self.player_cards2)
                print()
                print ('-------------------------GAME_OVER------------------------')
                print()
                break 

            if self.player_cards1 == [] or self.player_cards2 == []:
        
                print('Гравець 1 :',self.player_cards1,'Гравець 2 :',self.player_cards2)
                print ('-------------------------GAME_OVER------------------------')
                break

            
    
            print('Гравець 1 :',self.player_cards1, '||', 'СТІЛ :', self.stil, '||','Гравець 2 :', self.player_cards2)

        print()
        print('Карти на столі :', self.stil)
        print()
        print('Сума очок :', sum(self.stil))
        print()

        if sum(self.stil) % 2 == 0:
            print("Переможець : Гравець № 1")
            print()
        elif sum(self.stil) != 0:
            print("Переможець : Гравець № 2")
            print()
        else:
            print('error')
          
Players = Player('Петро', 'Катя')
Players.rozdacha_kart()
Players.vyvid()
Players.start()


'''
game = Game(Player_1, Player_2)
game.start()
'''



    

